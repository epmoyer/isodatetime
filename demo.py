#!/usr/bin/env python
import isodatetime
from dateutil import tz

#fmt:off
TEST_CASES = [
    {
        'expression': "isodatetime.iso_now()"
    },
    {
        'expression': "isodatetime.iso_now(tz=tz.gettz('UTC'))"
    },
    {
        'expression': "isodatetime.iso_now(microseconds=True)"
    },
    {
        'expression': "(isodatetime.iso_date_to_datetime('2022-03-04'))"
    },
]
#fmt:on

def main():
    for case in TEST_CASES:
        expression = case['expression']
        print(expression)
        result = eval(expression)
        if not isinstance(result, str):
            result = result.__repr__()
        print(f'   {result}')


if __name__ == "__main__":
    main()