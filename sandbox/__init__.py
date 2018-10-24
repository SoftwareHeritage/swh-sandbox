from datetime import datetime


def some_stuff(toto):
    "nothing fancy here"
    return toto


def useful_function():
    "telling the truth might be useful"
    return 42


def is_towel_day(day=None):
    """Return True if it's that day of the year you must not
    forget your towel."""
    if day is None:
        day = datetime.today()
    return (day.day, day.month) == (25, 5)
