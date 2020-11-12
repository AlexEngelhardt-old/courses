from x1_check_brackets import find_mismatch


def test_strings():
    assert find_mismatch("[]") == "Success"
    assert find_mismatch("{}[]") == "Success"
    assert find_mismatch("[()]") == "Success"
    assert find_mismatch("(())") == "Success"
    assert find_mismatch("{[]}()") == "Success"
    assert find_mismatch("{") == 1
    assert find_mismatch("{[}") == 3
    assert find_mismatch("foo(bar);") == "Success"
    assert find_mismatch("foo(bar[i);") == 10

