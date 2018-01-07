def f_to_c(fahrenheit):
	"""Converts Fahrenheit to Celsius
	
	>>> f_to_c(14)
	-10.0
	>>> f_to_c(68)
	20.0
	>>> f_to_c(-31)
	-35.0
	"""
	return (fahrenheit - 32) * 5 / 9
	
def c_to_f(celsius):
	"""Converts Celsius to Fahrenheit
	
	>>> c_to_f(0)
	32.0
	>>> c_to_f(5)
	41.0
	>>> c_to_f(-25)
	-13.0
	"""
	return celsius * 9 / 5 + 32
	
def dispatch_function(option1, f1, option2, f2):
	"""Takes in two options and two functions. Returns a function which returns either f1 or f2 on a given number depending on a given option
	
	>>> func_d = dispatch_function('c to f', c_to_f, 'f to c', f_to_c)
	>>> func_d('c to f', 0)
	32.0
	>>> func_d('f to c', 68)
	20.0
	"""
	
	def doer(option, number):
		assert option == option1 or option == option2
		if option == option1:
			return f1(number)
		elif option == option2:
			return f2(number)
	return doer
	
def make_buzzer(n):
	"""Returns a function that prints numbers in a specified
	range except those divisible by n
	
	>>> i_hate_fives = make_buzzer(5)
	>>> i_hate_fives(10)
	Buzz!
	1
	2
	3
	4
	Buzz!
	6
	7
	8
	9
	"""
	def counter(x):
		for i in range(x):
			if i % 5 == 0:
				print("Buzz!")
			else:
				print(i)
	return counter

# Draw environment diagrams on the function calls below
# Note: Successfully estimated return values of 5 and 6 :)
g = lambda x: x + 3
def wow(f):
	def boom(g):
		return f(g)
	return boom

f = wow(g)
# will return 5
f(2)

g = lambda x: x * x
# will return 6
f(3)


def lambda_curry2(func):
	"""Return a curried ersion of a two argument function
	>>> from operator import add
	>>> x = lambda_curry2(add)
	>>> y = x(3)
	>>> y(5)
	8
	"""
	return lambda x: lambda y: func(x, y)
	
def funception(func_a, start):
	"""Takes in a function A and start value.
	Returns a function B that will find the product of
	function A applied to the range of numbers from
	start (inclusive) to stop (exclusive)
	
	>>> func_a = lambda num: num + 1
	>>> func_b1 = funception(func_a, 3)
	>>> func_b1(2)
	4
	
	This one was very mysterious ;\
	"""
	def func_b(stop):
		puf = start
		if puf < 0:
			exit()
		elif puf > stop:
			return func_a(puf)
		product = 0
		while puf < stop:
			product += func_a(puf)
			puf += 1
		return product
	return func_b


from itertools import cycle as iter_cycle
	
def cycle(f1, f2, f3):
	"""
	Returns a function that is itself a higher order function
	>>> def add1(x):
	...     return x + 1
	>>> def times2(x):
	...     return x * 2
	>>> def add3(x):
	...     return x + 3
	>>> my_cycle = cycle(add1, times2, add3)
	>>> identity = my_cycle(0)
	>>> identity(5)
	5
	>>> add_one_then_double = my_cycle(2)
	>>> add_one_then_double(1)
	4
	>>> do_all_functions = my_cycle(3)
	>>> do_all_functions(2)
	9
	>>> do_more_than_a_cycle = my_cycle(4)
	>>> do_more_than_a_cycle(2)
	10
	>>> do_two_cycles = my_cycle(6)
	>>> do_two_cycles(1)
	19
	
	The boring implementation of yet_another:
	for i in range(n):
		if i % 3 == 0:
			x = f1(x)
		elif i % 3 == 1:
			x = f2(x)
		elif i % 3 == 2:
			x = f3(x)
	return x
	
	Yet a more concise version is more general, the one with *args would be
	even sexier :)
	"""
	
	def another(n):
		def yet_another(x):
			bicycle = iter_cycle((f1, f2, f3,))
			for _ in range(n):
				x = bicycle.__next__()(x)
			return x
		return yet_another
	return another

