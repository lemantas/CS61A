"""Extra questions for lab 2."""

# Q9
def gets_discount(x, y):
    """ Returns True if this is a combination of a senior citizen
    and a child, False otherwise.

    >>> gets_discount(65, 12)
    True
    >>> gets_discount(9, 70)
    True
    >>> gets_discount(40, 45)
    False
    >>> gets_discount(40, 75)
    False
    >>> gets_discount(65, 13)
    False
    >>> gets_discount(7, 9)
    False
    >>> gets_discount(73, 77)
    False
    >>> gets_discount(70, 31)
    False
    >>> gets_discount(10, 25)
    False
    """
    "*** YOUR CODE HERE ***"
    return (x >= 65 or y >= 65) and (x <= 12 or y <= 12)


# Q10
def is_factor(x, y):
    """ Returns True if x is a factor of y, False otherwise.

    >>> is_factor(3, 6)
    True
    >>> is_factor(4, 10)
    False
    >>> is_factor(0, 5)
    False
    >>> is_factor(0, 0)
    False
    """
    "*** YOUR CODE HERE ***"
    if x == 0:
    	return False
    return not y % x


# Q11
def falling(n, k):
	"""Compute the falling factorial of n to depth k.

	>>> falling(6, 3)  # 6 * 5 * 4
	120
	>>> falling(4, 0)
	1
	>>> falling(4, 3)  # 4 * 3 * 2
	24
	>>> falling(4, 1)  # 4
	4
	"""
	"*** YOUR CODE HERE ***"
	factorial = 1
	for _ in range(k):
		factorial = factorial * n
		n -= 1
	return factorial

