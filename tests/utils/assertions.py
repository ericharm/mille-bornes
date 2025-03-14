def assert_exception_matches(actual_exception: Exception, expected_exception: Exception) -> None:
    assert actual_exception.__class__ == expected_exception.__class__
    assert actual_exception.args == expected_exception.args
