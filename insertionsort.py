"""Given a list, sort it using insertion sort.

For example::

    >>> from random import shuffle
    >>> alist = list(range(1, 11))

    >>> shuffle(alist)
    >>> insertion_sort(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> shuffle(alist)
    >>> insertion_sort(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> shuffle(alist)
    >>> insertion_sort(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""


def insertion_sort(alist):
    """Given a list, sort it using insertion sort."""

    for i in range(1, len(alist)):
        #assign in every iteration
        k = i
        #if current element more then previous element
        while k > 0 and alist[k-1] > alist[k]:
            alist[k], alist[k-1] = alist[k-1], alist[k]
            k-= 1
    return alist         


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. NICE SORTING!\n")
