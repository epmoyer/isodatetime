from datetime import datetime

LOGURU_FORMAT_ISO = "{time:YYYY-MM-DD}T{time:HH:mm:ss.SSSZZ} | {level:<8} | {message}"
LOGURU_FORMAT_ISO_UTC = "{time:YYYY-MM-DD!UTC}T{time:HH:mm:ss.SSS!UTC}Z | {level:<8} | {message}"


def datetime_to_iso_datetime(datetime_object, tz=None, microseconds=False):
    """Convert datetime.datetime object to ISO datetime of form YYYY-MM-DDTHH:MM:SS[+/-]FF:FF.

    Args:
        tz (tzfile or datetime.timezone):
            A  tzfile object (such as returned dateutil.tz.gettz())

            OR

            A datetime.timezone object (such as returned by 
                datetime.timezone() or datetime.timezone.utc())

        microseconds(bool):
            If True, then microseconds will be included in the returned
            iso time string (YYYY-MM-DDTHH:MM:SS.MMMMMM[+/-]FF:FF)

    If tz is None (default), then the current system timezone will be used.
    """
    dt = datetime_object.astimezone(tz)
    if not microseconds:
        dt = dt.replace(microsecond=0)
    return dt.isoformat()


def datetime_to_iso_date(datetime_object):
    """Convert datetime.datetime object to ISO date of form YYYY-MM-DD."""
    return datetime_object.strftime(r"%Y-%m-%d")


def iso_date_to_datetime(iso_date):
    """Convert ISO date of form YYYY-MM-DD to datetime.datetime object."""
    return datetime.strptime(iso_date, r"%Y-%m-%d")


def iso_date_to_date(iso_date):
    """Convert ISO date of form YYYY-MM-DD to datetime.date object."""
    return datetime.strptime(iso_date, r"%Y-%m-%d").date()


def iso_datetime_now(tz=None, microseconds=False):
    """Return the current date and time as an iso datetime.

    (For options, see datetime_to_iso_datetime)
    """
    return datetime_to_iso_datetime(datetime.now(), tz=tz, microseconds=microseconds)


def iso_date_now(tz=None):
    """Return the current date as an iso date.
    
    (For options, see datetime_to_iso_datetime)
    """
    return datetime_to_iso_datetime(datetime.now(), tz=tz)[:10]


def iso_datetime_to_filesafe(iso_datetime):
    """Convert an iso datetime to a filename-safe string.

    The returned string will contain only characters suitable for inclusion in filename
        "2023-01-20T10:53:59+08:00" ->
        "2023-01-20T10_53_59P08_00"
    """
    return iso_datetime.replace(':', '_').replace('+', 'P')
