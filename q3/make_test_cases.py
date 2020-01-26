#!/usr/bin/env python3

# q3

import os.path


def to_pathname(filename):
    return os.path.join(os.path.dirname(__file__), filename)


def write_case(case_id: int, case):
    case_id = f"{case_id:02d}"
    a, b, c, result = case
    intext = f"{a}\n{b}\n{c}\n"
    in_filename = f"test-cases/input{case_id}.txt"
    with open(to_pathname(in_filename), 'w') as ofile:
        ofile.write(intext)
    extext = f"""\
Please enter value of a: {a}
Please enter value of b: {b}
Please enter value of c: {c}
This equation has {result}
"""
    ex_filename = f"test-cases/expected-output{case_id}.txt"
    with open(to_pathname(ex_filename), 'w') as ofile:
        ofile.write(extext)
    print(f"{in_filename} and {ex_filename} written")


def main():
    test_cases = [
        (1, 4, 4, 'a single real solution x=-2'),
        (0, -2, 6, 'a single real solution x=3'),
        (0, 2, 15, 'a single real solution x=-7.5'),
        (1, 0, 4, 'no real solution'),
        (1, 1, 1, 'no real solution'),
        (0, 0, 4, 'no solution'),
        (0, 0, -1.5, 'no solution'),
        (0, 0, 0, 'an infinite number of solutions'),
        (1, 1, -2, 'two real solutions: x=1 and x=-2'),
        (4, 4, -3, 'two real solutions: x=0.5 and x=-1.5'),
        (4, 1, -3, 'two real solutions: x=0.75 and x=-1'),
        (2, -11, -21, 'two real solutions: x=7 and x=-1.5'),
    ]
    for i, test_case in enumerate(test_cases):
        write_case(i + 1, test_case)


if __name__ == '__main__':
    exit(main())
