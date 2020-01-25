#!/usr/bin/env python3

import os.path


def to_pathname(filename):
    return os.path.join(os.path.dirname(__file__), filename)


def write_case(case_id: int, case):
    case_id = f"{case_id:02d}"
    w, h, status = case
    intext = f"{w}\n{h}\n"
    in_filename = f"input{case_id}.txt"
    with open(to_pathname(in_filename), 'w') as ofile:
        ofile.write(intext)
    extext = f"""\
Please enter weight (in pounds): {w}
Please enter height (in inches): {h}
The weight status is: {status}
"""
    ex_filename = f"expected-output{case_id}.txt"
    with open(to_pathname(ex_filename), 'w') as ofile:
        ofile.write(extext)
    print(f"{in_filename} and {ex_filename} written")


def main():
    test_cases = [
        (105.3, 66, 'Underweight'),
        (100.6, 62, 'Underweight'),
        (114.62032787174377, 66, 'Normal'),     # BMI 18.5
        (140.4, 67, 'Normal'),      # BMI 22
        (149.63324948411787, 65, 'Normal'),      # BMI 24.9
        (154.89233496181592, 66, 'Overweight'),  # BMI 25
        (202.475004, 69, 'Overweight'),          # BMI 29.9
        (172.4, 67, 'Overweight'),  # BMI 27
        (164.067, 61, 'Obese'),     # BMI 30
        (277, 78, 'Obese'),         # BMI 32
    ]
    for i, test_case in enumerate(test_cases):
        write_case(i + 1, test_case)


if __name__ == '__main__':
    exit(main())
