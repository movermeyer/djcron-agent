from djcron_agent import versions


def test_version_is_iterable():
    assert isinstance(versions.__version__, tuple)


def test_app_has_a_version_string():
    assert isinstance(versions.APP.version, str)

def test_app_has_a_description():
    assert isinstance(versions.APP.description, str)
