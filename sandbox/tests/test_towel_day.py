from datetime import datetime
from sandbox import is_towel_day


def test_towel_day():
    assert is_towel_day(datetime(2011, 5, 25))
    assert not is_towel_day(datetime(2011, 6, 25))
    assert not is_towel_day(datetime(2011, 5, 26))
