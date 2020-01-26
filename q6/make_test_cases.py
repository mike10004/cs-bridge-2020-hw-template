#!/usr/bin/env python3

# q6

import os.path


def to_pathname(filename):
    return os.path.join(os.path.dirname(__file__), filename)


def write_case(case_id: int, case):
    case_id = f"{case_id:02d}"
    day, time, duration, cents = case
    intext = f"{day}\n{time}\n{duration}\n"
    in_filename = f"test-cases/input{case_id}.txt"
    with open(to_pathname(in_filename), 'w') as ofile:
        ofile.write(intext)
    extext = f"""\
Enter day of week call was started: {day}
Enter time of day call was started (24-hour format): {time}
Enter length of call in minutes: {duration}
Cost of call: {cents // 100} dollars and {cents % 100} cents
"""
    ex_filename = f"test-cases/expected-output{case_id}.txt"
    with open(to_pathname(ex_filename), 'w') as ofile:
        ofile.write(extext)
    print(f"{in_filename} and {ex_filename} written")


def main():
    # wkday rate 0.40 cpm
    # wkngt rate 0.25 cpm
    # wkend rate 0.15 cpm
    test_cases = [
        ("Tu", "06:32", 24, 600),
        ("We", "08:00",  9, 9 * 40),
        ("We", "8:00",   7, 7 * 40),
        ("Fr", "17:59", 23, 23 * 40),
        ("Su", "00:30",  45, 45 * 15),
        ("Sa", "13:30",  25, 25 * 15),
        ("Mo", "18:01", 12, 12 * 25),
        ("Tu", "7:59", 54, 54 * 25),
        ("Th", "23:34", 4, 4 * 25),
    ]
    for i, test_case in enumerate(test_cases):
        write_case(i + 1, test_case)


if __name__ == '__main__':
    exit(main())
