#!/usr/bin/env python3


def write_case(id, name, gradyear, curryear, expected):
    intext = f"{name}\n{gradyear}\n{curryear}\n"
    with open(f"input{id}.txt", 'w') as ofile:
        print(intext, end="", file=ofile)
    extext = f"Please enter your name: {name}\nPlease enter your graduation year: {gradyear}\nPlease enter current year: {curryear}\n{name}, you are {expected}\n"
    with open(f"expected-output{id}.txt", 'w') as ofile:
        print(extext, end="", file=ofile)


def main():
    params = [
        ('Jessica', '2019', '2015', 'a Freshman'),
        ('Julia', '2023', '2020', 'a Sophomore'),
        ('Jennifer', '1985', '1983', 'a Junior'),
        ('Joanne', '1992', '1991', 'a Senior'),
        ('Jane', '2209', '2209', 'graduated'),
        ('Jillian', '2005', '1999', 'not in college yet')
    ]
    for i, param in enumerate(params):
        name, gradyear, curryear, expected = param
        write_case(i + 1, name, gradyear, curryear, expected)


if __name__ == '__main__':
    exit(main())
