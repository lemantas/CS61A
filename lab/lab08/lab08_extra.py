## Extra Linked Lists and Sets ##

from lab08 import *

# Set Practice

def add_up(n, lst):
    """Returns True if any two non identical elements in lst add up to any n.

    >>> add_up(100, [1, 2, 3, 4, 5])
    False
    >>> add_up(7, [1, 2, 3, 4, 2])
    True
    >>> add_up(10, [5, 5])
    False
    """
    "*** YOUR CODE HERE ***"
    uniques = set(lst)
    
    for member in uniques:
        other_num = n - member
        if other_num != member and other_num in uniques:
            return True
    return False

# pow with O(log n) efficiency
def square(x):
    return x * x

def pow(n,k):
    """Computes n^k.

    >>> pow(2, 3)
    8
    >>> pow(4, 2)
    16
    """
    "*** YOUR CODE HERE ***"
    if k == 0:
        return 1
    elif k % 2 == 0:
        return square(pow(n, k//2))
    else:
        return n * pow(n, k-1)

def missing_no(lst):
    """lst contains all the numbers from 1 to n for some n except some
    number k. Find k.

    >>> missing_no([1, 0, 4, 5, 7, 9, 2, 6, 3])
    8
    >>> missing_no(list(filter(lambda x: x != 293, list(range(2000)))))
    293
    """
    "*** YOUR CODE HERE ***"
    # full_set = set(range(max(lst)))
    # return list(full_set.difference(set(lst)))[0]
    # well, course's implementation is more elegant:
    return sum(range(max(lst) + 1)) - sum(lst)

def find_duplicates_k(k, lst):
    """Returns True if there are any duplicates in lst that are within k
    indices apart.

    >>> find_duplicates_k(3, [1, 2, 3, 4, 1])
    False
    >>> find_duplicates_k(4, [1, 2, 3, 4, 1])
    True
    """
    "*** YOUR CODE HERE ***"
    x, end = 0, len(lst) - 1
    while k <= end:
        if lst[x] == lst[k]:
            return True
        x += 1
        k += 1
    return False



