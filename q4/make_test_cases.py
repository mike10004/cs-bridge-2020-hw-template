#!/usr/bin/env python3

# q4

import os.path


def to_pathname(filename):
    return os.path.join(os.path.dirname(__file__), filename)


def write_case(case_id: int, case):
    case_id = f"{case_id:02d}"
    x, choice, x_rounded = case
    intext = f"{x}\n{choice}\n"
    in_filename = f"test-cases/input{case_id}.txt"
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
    ex_filename = f"test-cases/expected-output{case_id}.txt"
    with open(to_pathname(ex_filename), 'w') as ofile:
        ofile.write(extext)
    print(f"{in_filename} and {ex_filename} written")


def main():
    # C++ and Python differ on whether nearest negative is up or down.
    # For this question, we use the definition such that -1.5 rounds
    # to -2, per instructor reply at https://piazza.com/class/k548telxf692rm?cid=153
    # That is, the midpoint between two integers is rounded to the integer 
    # of greater magnitude.
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
        (-2.5, 3, -3),  # an example of rounding negative number to nearest integer (-2.5 down to -3)
        (-2.9, 1, -3),
        (-2.9, 2, -2),
        (-2.9, 3, -3),
        (-2, 1, -2),
        (-2, 2, -2),
        (-2, 3, -2),
        (-0.5, 1, -1),
        (-0.5, 2, 0),
        (-0.5, 3, -1),
        (0.5, 1, 0),
        (0.5, 2, 1),
        (0.5, 3, 1),
        (-0.25, 1, -1),
        (-0.25, 2, 0),
        (-0.25, 3, 0),
        (0.25, 1, 0),
        (0.25, 2, 1),
        (0.25, 3, 0),
        (-0.75, 1, -1),
        (-0.75, 2, 0),
        (-0.75, 3, -1),
        (0.75, 1, 0),
        (0.75, 2, 1),
        (0.75, 3, 1),
        (0, 1, 0),
        (0, 2, 0),
        (0, 3, 0),
        (1, 1, 1),
        (1, 2, 1),
        (1, 3, 1),
        (-1, 1, -1),
        (-1, 2, -1),
        (-1, 3, -1),
        (7, 1, 7),
        (7, 2, 7),
        (7, 3, 7),
        (-7, 1, -7),
        (-7, 2, -7),
        (-7, 3, -7),
        (0.499999975, 3, 0),
        (-0.499999975, 3, 0),
    ]
    for i, test_case in enumerate(test_cases):
        write_case(i + 1, test_case)


if __name__ == '__main__':
    exit(main())
