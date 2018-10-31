from swh.sandbox import useful_function


def test_useful_ok():
    assert useful_function() == 42, 'you forgot your towel!'
