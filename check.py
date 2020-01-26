#!/usr/bin/env python3.6

import logging
import threading
import sys
import uuid
import tempfile
import os.path
import subprocess
from subprocess import PIPE, DEVNULL
import glob
import time
from argparse import ArgumentParser
from typing import List, Tuple, Optional, NamedTuple


_log = logging.getLogger(__name__)
_SCREEN_START_DELAY_SECONDS = 2.0
_DEFAULT_PAUSE_DURATION_SECONDS = 0.5


class CommandException(Exception):
    pass


def read_file_text(pathname: str, ignore_failure=False) -> str:
    try:
        with open(pathname, 'r') as ifile:
            return ifile.read()
    except IOError:
        if not ignore_failure:
            raise


def read_file_lines(pathname: str) -> List[str]:
    with open(pathname, 'r') as ifile:
        return [line for line in ifile]


def _cmd(cmd_list, err_msg="Command Line Error", allow_nonzero_exit=False) -> str:
    proc = subprocess.run(cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if allow_nonzero_exit or proc.returncode != 0:
        raise CommandException("exit code {}; {}\n{}".format(proc.returncode, err_msg, proc.stderr.decode('utf8')))
    return proc.stdout.decode('utf8')


def detect_test_case_files(q_dir: str) -> List[Tuple[Optional[str], str]]:
    test_cases = []
    for root, dirs, files in os.walk(q_dir):
        for f in files:
            if f.startswith('input'):
                input_file = os.path.join(root, f)
                expected_file = os.path.join(root, "expected-output" + f[5:])
                test_cases.append((input_file, expected_file))
    if not test_cases:
        return [(None, os.path.join(q_dir, 'expected-output.txt'))]
    return test_cases


class TestCaseOutcome(NamedTuple):

    passed: bool
    executable: str
    input_file: Optional[str]
    expected_text: str
    actual_text: str
    message: str


class TestCaseRunner(object):

    def __init__(self, executable, pause_duration=_DEFAULT_PAUSE_DURATION_SECONDS):
        self.executable = executable
        self.pause_duration = pause_duration

    def _pause(self, duration=None):
        #_log.debug("sleeping for %s seconds", self.pause_duration)
        time.sleep(self.pause_duration if duration is None else duration)

    def run_test_case(self, input_file: Optional[str], expected_file: str):
        tid = threading.current_thread().ident
        expected_text = read_file_text(expected_file)

        def outcome(passed: bool, actual_text: Optional[str], message: str):
            return TestCaseOutcome(passed, self.executable, input_file, expected_text, actual_text, message)

        def check(actual_text: str):
            if actual_text != expected_text:
                return outcome(False, actual_text, "diff")
            return outcome(True, actual_text, "ok")

        if input_file is None:
            output = _cmd([self.executable])
            return check(output)
        
        input_lines = read_file_lines(input_file)
        case_id = str(uuid.uuid4())
        with tempfile.TemporaryDirectory() as tempdir:
            exitcode = subprocess.call(['screen', '-L', '-S', case_id, '-d', '-m', self.executable], cwd=tempdir)
            if exitcode != 0:
                return outcome(False, None, f"screen start failure {exitcode}")
            _log.debug("[%s] screen session %s started for %s; feeding lines from %s", tid, case_id, self.executable, os.path.basename(input_file))
            #self._pause(self.start_delay)
            #_log.debug("screen sessions: %s", _cmd(['screen', '-list']).split("\n"))
            completed = False
            try:
                screenlog = os.path.join(tempdir, 'screenlog.0')
                for i, line in enumerate(input_lines):
                    self._pause()
                    _log.debug("[%s] feeding line %s to process: %s", tid, i+1, line.strip())
                    proc = subprocess.run(['screen', '-S', case_id, '-X', 'stuff', line], stdout=PIPE, stderr=PIPE)  # note: important that line has terminal newline char
                    if proc.returncode != 0:
                        stdout, stderr = proc.stdout.decode('utf8'), proc.stderr.decode('utf8')
                        msg = f"[{tid}] stuff exit code {proc.returncode} feeding line {i+1}; stderr={stderr}; stdout={stdout}"
                        _log.debug(msg)
                        return outcome(False, read_file_text(screenlog, True), msg)
                completed = True
            finally:
                self._pause()
                exitcode = subprocess.call(['screen', '-S', case_id, '-X', 'quit'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)  # ok if failed; probably already terminated
                # if not completed and exitcode != 0:
                #     _log.warning("screen 'quit' failed with code %s", exitcode)
            output = read_file_text(screenlog).replace("\r\n", "\n")
        return check(output)


def check_cpp(cpp_file: str, concurrency_level: int, pause_duration: float, max_test_cases:int):
    q_dir = os.path.dirname(cpp_file)
    q_name = os.path.basename(q_dir)
    q_executable = os.path.join(q_dir, 'cmake-build', q_name)
    assert os.path.isfile(q_executable), "not found: " + q_executable
    test_case_files = detect_test_case_files(q_dir)
    runner = TestCaseRunner(q_executable, pause_duration)
    outcomes = {}
    outcomes_lock = threading.Lock()
    threads: List[threading.Thread] = []
    concurrer = threading.Semaphore(concurrency_level)
    for i, test_case in enumerate(test_case_files):
        if max_test_cases is not None and i >= max_test_cases:
            _log.debug("breaking early due to test case limit")
            break
        input_file, expected_file = test_case
        def perform():
            concurrer.acquire()
            try:
                outcome = runner.run_test_case(input_file, expected_file)
                _log.info("%s: case %s: pass? %s; message=%s", q_name, i + 1, outcome.passed, outcome.message)
            finally:
                concurrer.release()
            outcomes_lock.acquire()
            try:
                outcomes[test_case] = outcome
            finally:
                outcomes_lock.release()
        t = threading.Thread(target=perform)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    failures = [outcome for outcome in outcomes.values() if not outcome.passed]
    if failures:
        print(f"{len(failures)} of {len(outcomes)} tests failed", file=sys.stderr)


def main():
    parser = ArgumentParser()
    parser.add_argument("subdirs", nargs='*', help="subdirectories containing executables to test; if none specified, run all")
    parser.add_argument("-l", "--log-level", metavar="LEVEL", choices=('DEBUG', 'INFO', 'WARNING', 'ERROR'), default='INFO', help="set log level")
    parser.add_argument("-p", "--pause", type=float, metavar="DURATION", help="pause duration (seconds)", default=_DEFAULT_PAUSE_DURATION_SECONDS)
    parser.add_argument("-m", "--max-cases", type=int, default=None, metavar="N", help="run at most N test cases per cpp")
    parser.add_argument("-j", "-t", "--threads", type=int, default=4, metavar="N", help="concurrency level for test cases")
    args = parser.parse_args()
    logging.basicConfig(level=logging.__dict__[args.log_level])
    this_file = os.path.abspath(__file__)
    proj_dir = os.path.dirname(this_file)  # also might want to handle the case where script piped in on stdin
    _log.debug("this project dir is %s, derived from %s", proj_dir, os.path.basename(this_file))
    assert proj_dir and os.path.isdir(proj_dir), "failed to detect project directory"
    build_script = os.path.join(proj_dir, 'build.sh')
    _log.debug("building executables by running %s", build_script)
    _cmd(['bash', build_script], err_msg="build error")
    _log.debug("done building executables")
    main_cpps = []
    if args.subdirs:
        _log.debug("limiting tests to subdirectories: %s", args.subdirs)
        main_cpps += [os.path.join(proj_dir, subdir, 'main.cpp') for subdir in args.subdirs]
    else:
        _log.debug("searching %s for main.cpp files", proj_dir)
        for root, dirs, files in os.walk(proj_dir):
            for f in files:
                if f == 'main.cpp':
                    main_cpps.append(os.path.join(root, f))
    if not main_cpps:
        _log.error("no main.cpp files found")
        return 1
    for i, cpp_file in enumerate(sorted(main_cpps)):
        check_cpp(cpp_file, args.threads, args.pause, args.max_cases)
    return 0


if __name__ == '__main__':
    exit(main())
