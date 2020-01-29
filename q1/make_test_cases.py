#!/usr/bin/env python3

# q1

import os.path
from typing import NamedTuple


def to_pathname(filename, disable_mkdir=False):
    pathname = os.path.join(os.path.dirname(__file__), 'test-cases', filename)
    if not disable_mkdir:
        os.makedirs(os.path.dirname(pathname), exist_ok=True)
    return pathname


class TestCase(NamedTuple):
    
    item1_price: str
    item2_price: str
    club_card: str
    tax_rate: str
    base_price: str
    discount_price: str
    total_price: str
    


def write_case(case_id: int, case: TestCase):
    case_id = f"{case_id}"
    intext = f"{case.item1_price}\n{case.item2_price}\n{case.club_card}\n{case.tax_rate}\n"
    in_filename = f"input{case_id}.txt"
    with open(to_pathname(in_filename), 'w') as ofile:
        ofile.write(intext)
    extext = f"""\
Enter price of first item: {case.item1_price}
Enter price of second item: {case.item2_price}
Does customer have a club card? (Y/N): {case.club_card}
Enter tax rate, e.g. 5.5 for 5.5% tax: {case.tax_rate}
Base price: {case.base_price}
Price after discounts: {case.discount_price}
Total price: {case.total_price}
"""
    ex_filename = f"expected-output{case_id}.txt"
    with open(to_pathname(ex_filename), 'w') as ofile:
        ofile.write(extext)
    print(f"{in_filename} and {ex_filename} written")


def main():
    test_cases = [
        TestCase("10", "20", "y", "8.25", "30.00", "22.50", "24.36"),
        TestCase("5", "14", "yes", "7.0", "19.00", "14.85", "15.89"),
        TestCase("6", "25", "N", "8.25", "31.00", "28.00", "30.31"),
        TestCase("10", "0", "y", "20.0", "10.00", "9.00", "10.80"),
        TestCase("0", "10", "Y", "20.0", "10.00", "9.00", "10.80"),
    ]
    for i, test_case in enumerate(test_cases):
        write_case(i + 1, test_case)


if __name__ == '__main__':
    exit(main())
