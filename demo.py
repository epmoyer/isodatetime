#!/usr/bin/env python

# Standard Library
import datetime
from dateutil import tz
import sys

# Library
from rich.console import Console
from rich.theme import Theme
from loguru import logger

# Local
from isodatetime import (
    datetime_to_iso_datetime,
    datetime_to_iso_date,
    iso_date_to_datetime,
    iso_date_to_date,
    iso_now,
    iso_datetime_filesafe,
    LOGURU_FORMAT_ISO,
    LOGURU_FORMAT_ISO_UTC
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
FUNCTION_EXAMPLES = [
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
    # iso_datetime_filesafe()
    # -------------------------------
    {
        'heading': "iso_datetime_filesafe()",
        'expression': "iso_datetime_filesafe('2023-01-20T10:53:59-08:00')",
    },
    {
        'expression': "iso_datetime_filesafe('2023-01-20T10:53:59+08:00')",
    },
]
# fmt:on

# fmt:off
LOGURU_EXAMPLES = [
    {
        'heading': 'loguru logging with format: LOGURU_FORMAT_ISO',
        'format': LOGURU_FORMAT_ISO
    },
    {
        'heading': 'loguru logging with format: LOGURU_FORMAT_ISO_UTC',
        'format': LOGURU_FORMAT_ISO_UTC
    }
]
# fmt:off
def main():
    for case in FUNCTION_EXAMPLES:
        show_heading(case)
        expression = case['expression']
        print(f'   [expression]{expression}[/expression]')
        result = eval(expression)
        if isinstance(result, str):
            result = f'[text]{result}[/text]'
        else:
            result = f'[object]{result.__repr__()}[/object]'
        print(f'      {result}')

    for case in LOGURU_EXAMPLES:
        show_heading(case)
        logger.remove()
        logger.add(
            sys.stdout,
            format=case['format']
        )
        logger.info('(example log message)')

def show_heading(case):
    heading = case.get('heading')
    if heading:
        print('-' * 80)
        print(f'{heading}')


if __name__ == "__main__":
    main()
