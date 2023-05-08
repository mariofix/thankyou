from .thankyou import give_thanks


def test_thanks():
    thanks_string = give_thanks()
    assert isinstance(thanks_string, str)
