#!/usr/bin/env python3

import os.path


def to_pathname(filename):
    return os.path.join(os.path.dirname(__file__), filename)


def write_case(case_id: int, case):
    case_id = f"{case_id:02d}"
    x, choice, x_rounded = case
    intext = f"{x}\n{choice}\n"
    in_filename = f"input{case_id}.txt"
    with open(to_pathname(in_filename), 'w') as ofile:
        ofile.write(intext)
    extext = f"""\
Please enter a Real number:
{x}
Choose your rounding method:
1. Floor round
2. Ceiling round
3. Round to the nearest whole number
{choice}
{x_rounded}
"""
    ex_filename = f"expected-output{case_id}.txt"
    with open(to_pathname(ex_filename), 'w') as ofile:
        ofile.write(extext)
    print(f"{in_filename} and {ex_filename} written")


def main():
    test_cases = [
        (4.78, 2, 5),
        (2.3, 1, 2),
        (2.3, 2, 3),
        (2.3, 3, 2),
        (2.5, 1, 2),
        (2.5, 2, 3),
        (2.5, 3, 3),
        (2.9, 1, 2),
        (2.9, 2, 3),
        (2.9, 3, 3),
        (-2.3, 1, -3),
        (-2.3, 2, -2),
        (-2.3, 3, -2),
        (-2.5, 1, -3),
        (-2.5, 2, -2),
        (-2.5, 3, -3),  # c++ and python differ on whether nearest negative is up or down
        (-2.9, 1, -3),
        (-2.9, 2, -2),
        (-2.9, 3, -3),
    ]
    for i, test_case in enumerate(test_cases):
        write_case(i + 1, test_case)


if __name__ == '__main__':
    exit(main())
