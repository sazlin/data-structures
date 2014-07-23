def sort(list):
    """
    performs insertion sort on list in place
    source: http://en.wikipedia.org/wiki/Insertion_sort
    """

    for i in xrange(1, len(list)):
        x = list[i]
        j = i
        while j > 0 and list[j-1] > x:
            list[j] = list[j-1]
            j -= 1
        list[j] = x


if __name__ == '__main__':
    import timeit
    import matplotlib.pyplot as plt

    repetitions = 10

    long_random_list_test = """
        l = [random.randint(-99999,99999) for i in xrange(0, 1000)]
        insertion_sort.sort(l)
        """
    long_random_time = timeit.timeit(
        long_random_list_test,
        setup="import insertion_sort, random",
        number=repetitions
    )
    print "1000 item random int list with {} repetitions takes time {}".format(
        repetitions, long_random_time)

    descend_case = """
        l = [i for i in xrange({}, 0, -1)]
        insertion_sort.sort(l)
        """

    ascend_case = """
        l = [i for i in xrange(0, {})]
        insertion_sort.sort(l)
        """

    descend_results = []
    ascend_results = []
    for size in xrange(50, 2501, 50):
        descend_time = timeit.timeit(
            descend_case.format(size),
            setup="import insertion_sort",
            number=repetitions
        )
        descend_results.append((size, descend_time))

        ascend_time = timeit.timeit(
            ascend_case.format(size),
            setup="import insertion_sort",
            number=repetitions
        )
        ascend_results.append((size, ascend_time))

    plt.hold(True)
    for i in range(len(descend_results)):
        n_descend, time_descend = descend_results[i]
        n_ascend, time_ascend = ascend_results[i]
        plt.plot(n_descend, time_descend, 'bo')
        plt.plot(n_ascend, time_ascend, 'ro')
    plt.show()
