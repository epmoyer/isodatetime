#!/usr/bin/env python

# Standard Library
import datetime
from dateutil import tz

# Library
from rich.console import Console
from rich.theme import Theme

# Local
from isodatetime import (
    datetime_to_iso_datetime,
    datetime_to_iso_date,
    iso_date_to_datetime,
    iso_date_to_date,
    iso_now,
)
# --------------------
# Rich output console
# --------------------
# fmt: off
THEME = Theme({
    "expression": "#00ff00",
    "text": "#ffff00",
    "object": "#00ffff",
})
# fmt: on
CONSOLE = Console(highlight=False, color_system='256', theme=THEME)
CONSOLE_PPRINT = Console(highlight=True, color_system='256', theme=THEME)
print_native = print
print = CONSOLE.print
pprint = CONSOLE_PPRINT.print


# fmt:off
TEST_CASES = [
    # -------------------------------
    # datetime_to_iso_datetime()
    # -------------------------------
    {
        'heading': "datetime_to_iso_datetime()",
        'expression': "datetime_to_iso_datetime(datetime.datetime(2022, 5, 6, 12, 34, 56))",
    },
    {
        'expression': "datetime_to_iso_datetime(datetime.datetime(2022, 5, 6, 12, 34, 56), tz=tz.gettz('UTC'))",
    },
    {
        'expression': "datetime_to_iso_datetime(datetime.datetime(2022, 5, 6, 12, 34, 56, 9876), microseconds=True)",
    },
    # -------------------------------
    # datetime_to_iso_date()
    # -------------------------------
    {
        'heading': "datetime_to_iso_date()",
        'expression': "datetime_to_iso_date(datetime.datetime(2022, 5, 6, 12, 34, 56))",
    },
    # -------------------------------
    # iso_date_to_datetime()
    # -------------------------------
    {
        'heading': "iso_date_to_datetime()",
        'expression': "iso_date_to_datetime('2022-05-06')",
    },
    # -------------------------------
    # iso_date_to_date()
    # -------------------------------
    {
        'heading': "iso_date_to_date()",
        'expression': "iso_date_to_date('2022-05-06')",
    },
    # -------------------------------
    # iso_now()
    # -------------------------------
    {
        'heading': "iso_now()",
        'expression': "iso_now()",
    },
    {
        'expression': "iso_now(tz=tz.gettz('UTC'))",
    },
    {
        'expression': "iso_now(microseconds=True)",
    },
    # -------------------------------
    # iso_date_to_datetime()
    # -------------------------------
    {
        'heading': "iso_date_to_datetime()",
        'expression': "iso_date_to_datetime('2022-03-04')"
    },
]
# fmt:on


def main():
    for i, case in enumerate(TEST_CASES):
        heading = case.get('heading')
        if heading:
            if i != 0:
                print()
            print(f'{heading}')
        expression = case['expression']
        print(f'   [expression]{expression}[/expression]')
        result = eval(expression)
        if isinstance(result, str):
            result = f'[text]{result}[/text]'
            # print(f'      [text]{result}[/text]')
        else:
            result = f'[object]{result.__repr__()}[/object]'
            # pprint(result)
            # result = result.__repr__()
        print(f'      {result}')


if __name__ == "__main__":
    main()
