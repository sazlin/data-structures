def quick_sort(values):
    """simple quick sort implementation"""
    if len(values) == 0:
        return []
    elif len(values) == 1:
        return values
    elif len(values) == 2:
        if values[0] > values[1]:
            return values[::-1]
        else:
            return values
    pivot = values[0]
    less_list = [x for x in values if x < pivot]
    more_list = [x for x in values if x > pivot]
    same_list = [x for x in values if x == pivot]  # keep track of dupes
    less_list = less_list + same_list
    if len(more_list) == 0:
        more_list.append(less_list.pop())
    return quick_sort(less_list) + quick_sort(more_list)

if __name__ == '__main__':
    import timeit
    print "Quick Sort | Worst Case |",\
        timeit.timeit(
            setup="""
from quick_sort import quick_sort
worst_case_values = [i for i in xrange(100,1,-1)]
        """,
            stmt="quick_sort(worst_case_values)",
            number=100)

    print "Quick Sort | Best Case |",\
        timeit.timeit(
            setup="""
from quick_sort import quick_sort
best_case_values = [i for i in xrange(1,100,1)]
        """,
            stmt="quick_sort(best_case_values)",
            number=100)
