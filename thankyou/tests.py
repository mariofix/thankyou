from .thankyou import give_thanks


def test_thanks_string():
    thanks_string = give_thanks()
    assert isinstance(thanks_string, str)


def test_thanks_tuple():
    thanks_string = give_thanks(as_tuple=True)
    assert isinstance(thanks_string, tuple)
