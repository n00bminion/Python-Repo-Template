import test_package


def test_import():
    """Package imports without error."""
    assert test_package is not None
