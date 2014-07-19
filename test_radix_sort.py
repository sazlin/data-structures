import pytest
from radix_sort import radix_sort_int, radix_sort_strings

def test_radix_sort_int():
    case_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    case_2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    case_3 = [7, 2, 5, 9, 1, 8, 0, 6, 4, 3]
    expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert radix_sort_int(case_1) == expected
    assert radix_sort_int(case_2) == expected
    assert radix_sort_int(case_3) == expected

def test_radix_sort_int_2():
    case_1 = [2345234, 98756473, 2234562,
                   365, 4, 22345, 63456354, 76789,
                   0000, 9223432]
    expected = list(case_1)
    expected.sort()
    assert radix_sort_int(case_1) == expected

def test_radix_sort_string():
    case_1 = ['a', 'aa', 'ab', 'aba', 'abb', 'z']
    case_2 = list(case_1)
    case_2.reverse()
    expected = ['a', 'aa', 'ab', 'aba', 'abb', 'z']
    assert radix_sort_strings(case_1) == expected
    assert radix_sort_strings(case_2) == expected

def test_radix_sort_string_2():
    case_1 = ['asdfjkba', 'g', 'poijlakbjbkasd', 'jns',
                    'zzzzzzzaaaz', 'asdz','mqioajoiba']
    expected = list(case_1)
    expected.sort()
    assert radix_sort_strings(case_1) == expected