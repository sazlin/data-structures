from itertools import chain
from math import log


def radix_sort_int(integers):
    """A simple LSD stable sort for base 10 integers"""
    #source: used wikipedia's article on radix sort for determining num_passes
    num_passes = int(round(log(max(abs(i) for i in integers), 10)) +1)
    sorted_integers = list(integers)
    for digit_pos in range(num_passes):
        sorting_buckets = [[] for i in range(10)]
        for integer in sorted_integers:
            bucket_index = (integer // 10 ** digit_pos) % 10
            sorting_buckets[bucket_index].append(integer)
        sorted_integers = list(chain.from_iterable(sorting_buckets))
    return sorted_integers

def radix_sort_strings(strings):
    """A simple MSD lexographic radix sort for strings"""
    num_chars = max(len(s) for s in strings)
    sorted_strings = list(strings)
    num_buckets = ord('z')  - ord('A')
    offset = ord('A')
    cur_digit = num_chars - 1
    while cur_digit >= 0:
        sorting_buckets = [[] for i in range( num_buckets  )]
        for s in sorted_strings:
            try:
                bucket_index = ord(s[cur_digit]) -1 - offset
            except IndexError as x:
                bucket_index = 0
            sorting_buckets[bucket_index].append(s)
        sorted_strings = list(chain.from_iterable(sorting_buckets))
        cur_digit -= 1
    return sorted_strings


if __name__ == '__main__':
    import timeit
    #worst case - integer
    t = timeit.timeit(
        setup="""
from radix_sort import radix_sort_int
list_of_ints = [ i for i in range(1000, 0, -1)]
list_of_ints.append(9999999999999999999999999999999999999)
""",
        stmt="radix_sort_int(list_of_ints)",
        number=100)
    print "Radix_sort_int | Worst Case |", t

    #best case - integer
    t = timeit.timeit(
        setup="""
from radix_sort import radix_sort_int
list_of_ints = [ i for i in range(0, 1000, 1)]
""",
        stmt="radix_sort_int(list_of_ints)",
        number=100)
    print "Radix_sort_int | Best Case |", t

    #worst case - string
    t = timeit.timeit(
        setup="""
from radix_sort import radix_sort_strings
list_of_strings = [chr(c) * 20 for c in range(ord('z'), ord('a')-1, -1)]
list_of_strings.append('z'*100)
""",
        stmt="radix_sort_strings(list_of_strings)",
        number=100)
    print "Radix_sort_string | Worst Case |", t

        #worst case - string
    t = timeit.timeit(
        setup="""
from radix_sort import radix_sort_strings
list_of_strings = [chr(c) * 20 for c in range(ord('a')-1, ord('z'), 1)]
""",
        stmt="radix_sort_strings(list_of_strings)",
        number=100)
    print "Radix_sort_string | Best Case |", t

    #semi random case
    random_case = [
        567756765,356734345345,
        5934534,
        1,
        2,
        6234234,
        44324,
        345345238,
        4564565,
        02424]
    sorted_random_case = radix_sort_int(random_case)
    #print sorted_random_case

    #best case
    best_case = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sorted_best_case = radix_sort_int(best_case)
    #print sorted_best_case

    #simple case
    simple_case = ['z', 'x', 'g', 'b', 'a', 'b']
    print radix_sort_strings(simple_case)

     #worst case
    worst_case = ['zzzzzzz', 'xxxxxxxx', 'xxxxxaxx', 'ca', 'c', 'bbbbbb']
    print radix_sort_strings(worst_case)
