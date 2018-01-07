# Q1
def skip_add(n):
	""" Takes a number x and returns x + x-2 + x-4 + x-6 + ... + 0.

	>>> skip_add(5)  # 5 + 3 + 1 + 0
	9
	>>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
	30
	"""
	"*** YOUR CODE HERE ***"
	if n <= 0:
		return 0
	else:
		return n + skip_add(n-2)

# Q6
def gcd(a, b):
	"""Returns the greatest common divisor of a and b.
	Should be implemented using recursion.

	>>> gcd(34, 19)
	1
	>>> gcd(39, 91)
	13
	>>> gcd(20, 30)
	10
	>>> gcd(40, 40)
	40
	"""
	"*** YOUR CODE HERE ***"
	if b > a:
		a, b = b, a
	if b == 0:
		return a
	else:
		return gcd(b, a % b)
	

# Q7
def hailstone(n):
	"""Print out the hailstone sequence starting at n, and return the
	number of elements in the sequence.

	>>> a = hailstone(10)
	10
	5
	16
	8
	4
	2
	1
	>>> a
	7
	"""
	"*** YOUR CODE HERE ***"
	if n == 1:
		print(n)
		return 1
	else:
		if n % 2 == 0:
			print(n)
			return 1 + hailstone(n//2)
		elif n % 2 == 1:
			print(n)
			return 1 + hailstone(n*3+1)

# Q8
def fibonacci(n):
	"""Return the nth fibonacci number.

	>>> fibonacci(11)
	89
	>>> fibonacci(5)
	5
	>>> fibonacci(0)
	0
	>>> fibonacci(1)
	1
	"""
	"*** YOUR CODE HERE ***"
	if n == 1:
		return 1
	elif n < 0:
		return 0
	else:
		return fibonacci(n-1) + fibonacci(n-2)

# Q9
def paths(m, n):
	"""Return the number of paths from one corner of an
	M by N grid to the opposite corner.

	>>> paths(2, 2)
	2
	>>> paths(5, 7)
	210
	>>> paths(117, 1)
	1
	>>> paths(1, 157)
	1
	"""
	"*** YOUR CODE HERE ***"
	if m == 1 or n == 1:
		return 1
	else:
		return paths(m-1, n) + paths(m, n-1)
	
def count_up(n):
	"""Print out all numbers up to and including n in ascending order.

	>>> count_up(5)
	1
	2
	3
	4
	5
	"""
	if n == 0:
		return
	count_up(n-1)
	print(n)

def skip_mul(n):
	"""Return the product of n * (n - 2) * (n - 4) * ...

	>>> skip_mul(5) # 5 * 3 * 1
	15
	>>> skip_mul(8) # 8 * 6 * 4 * 2  * 0
	0
	"""
	if n <= 0:
		return 1
	else:
		return n * skip_mul(n - 2)
		
def factorial(n):
	"""Return n * (n - 1) * (n - 2) * ... * 1.

	>>> factorial(5)
	120
	"""
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)
		
def print_up_to(n):
	"""Print every natural number up to n, inclusive.

	>>> print_up_to(5)
	1
	2
	3
	4
	5
	"""
	if n == 0:
		return
	else:
		print_up_to(n-1)
		print(n)
