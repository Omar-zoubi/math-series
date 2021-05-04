from math_series.series import fibonacci,lucas,sum_series
def test_fibonacci():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibonacci():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected
def test_fibonacci():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected


def test_lucas():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas():
    actual = lucas(1)
    expected = 1
    assert actual == expected
def test_lucas():
    actual = lucas(4)
    expected = 7
    assert actual == expected
