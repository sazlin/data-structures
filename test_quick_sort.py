import random
from quick_sort import quick_sort


def test_quick_sort():
    case_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    case_2 = list(case_1)
    case_2.reverse()
    expected = list(case_1)
    assert quick_sort(case_1) == expected
    assert quick_sort(case_2) == expected


def test_quick_sort_2():
    case_1 = [random.randrange(1000) for i in xrange(50)]
    expected = list(case_1)
    expected.sort()
    assert quick_sort(case_1) == expected


def test_quick_sort_3():
    case_1 = [5 for i in xrange(50)]
    expected = list(case_1)
    assert quick_sort(case_1) == expected
