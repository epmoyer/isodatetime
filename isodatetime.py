from datetime import datetime

def datetime_to_iso_datetime(datetime_object, tz=None, microseconds=False):
    """Convert datetime.datetime object to ISO datetime of form YYYY-MM-DDTHH:MM:SS[+/-}FF:FF.

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

def iso_now(tz=None, microseconds=False):
    return datetime_to_iso_datetime(datetime.now(), tz=tz, microseconds=microseconds)
