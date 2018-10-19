from datetime import datetime


def useful_function():
    return 42


def is_towel_day(day=None):
    if day is None:
        day = datetime.today()
    return (day.day, day.month) == (25, 5)
