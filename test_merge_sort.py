import merge_sort as m_sort


def test_empty_list():
    empty = []
    m_sort.sort(empty)
    assert empty == []


def test_sorted_list():
    sorted_list = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6]
    m_sort.sort(sorted_list)
    assert sorted_list == [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6]


def test_unsorted_list():
    unsorted_list = [6, 2, 8, 4, 5, 3, 3, 4, 88, 2, 99, -43, 0]
    m_sort.sort(unsorted_list)
    assert unsorted_list == [-43, 0, 2, 2, 3, 3, 4, 4, 5, 6, 8, 88, 99]
