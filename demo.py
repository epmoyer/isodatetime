#!/usr/bin/env python
import isodatetime 

#fmt:off
TEST_CASES = [
    {
        'expression': "isodatetime.iso_now()"
    }
]
#fmt:on

def main():
    # print("isodatetime.iso_now()")
    # print(f'   {isodatetime.iso_now()}')
    # print(eval("isodatetime.iso_now()"))

    for case in TEST_CASES:
        expression = case['expression']
        print(expression)
        print(f'   {eval(expression)}')


if __name__ == "__main__":
    main()