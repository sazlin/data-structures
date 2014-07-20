"""
adapted from 'The Object of Data Abstraction and Structures Using Java'
"""


def sort(a):
    do_merge_sort(a, 0, len(a)-1)


def do_merge_sort(a, lo, hi):
    if lo < hi:
        mid = (lo + hi) / 2
        do_merge_sort(a, lo, mid)
        do_merge_sort(a, mid+1, hi)
        merge(a, lo, hi)


def merge(a, lo, hi):
    mid = (lo + hi) / 2
    l_idx = lo
    r_idx = mid+1
    tmp = []
    tmp_idx = 0
    while (l_idx <= mid) and (r_idx <= hi):
        if a[l_idx] < a[r_idx]:
            tmp.append(a[l_idx])
            l_idx += 1
        else:
            tmp.append(a[r_idx])
            r_idx += 1
        tmp_idx += 1

    # copy remaining values from left list into tmp
    for j in xrange(l_idx, mid+1):
        tmp.append(a[j])
        tmp_idx += 1

    # copy remaining values from right list into tmp
    for j in xrange(r_idx, hi+1):
        tmp.append(a[j])
        tmp_idx += 1

    # copy tmp back into a
    for j in xrange(lo, hi+1):
        a[j] = tmp[j-lo]


if __name__ == '__main__':
    import sys
    import timeit
    import matplotlib.pyplot as plt

    repetitions = 10

    long_random_list_test = """
        l = [random.randint(-99999,99999) for i in xrange(0, 1000)]
        merge_sort.sort(l)
        """
    long_random_time = timeit.timeit(
        long_random_list_test,
        setup="import merge_sort, random",
        number=repetitions
    )
    print "1000 item random int list with {} repetitions takes time {}".format(
        repetitions, long_random_time)

    descend_case = """
        l = [i for i in xrange({}, 0, -1)]
        merge_sort.sort(l)
        """

    ascend_case = """
        l = [i for i in xrange(0, {})]
        merge_sort.sort(l)
        """

    descend_results = []
    ascend_results = []
    message = "{:.2%} of test list sizes done\r"
    min_list_size = 500
    max_list_size = 25000
    increment = 500
    for size in xrange(min_list_size, max_list_size+1, increment):
        descend_time = timeit.timeit(
            descend_case.format(size),
            setup="import merge_sort",
            number=repetitions
        )
        descend_results.append((size, descend_time))

        ascend_time = timeit.timeit(
            ascend_case.format(size),
            setup="import merge_sort",
            number=repetitions
        )
        ascend_results.append((size, ascend_time))
        sys.stdout.write(message.format(size / float(max_list_size)))
        sys.stdout.flush()

    plt.hold(True)
    for i in range(len(descend_results)):
        n_descend, time_descend = descend_results[i]
        n_ascend, time_ascend = ascend_results[i]
        plt.plot(n_descend, time_descend, 'bo')
        plt.plot(n_ascend, time_ascend, 'ro')
    plt.show()
