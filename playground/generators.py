class Naturals():
    def __init__(self):
        self.current = 0
        
    def __next__(self):
        result = self.current
        self.current += 1
        return result
        
    def __iter__(self):
        return self

from operator import add
        
class IterCombiner(object):
    """
    >>> comb = IterCombiner(Naturals(), Naturals(), add)
    >>> [next(comb) for _ in range(10)]
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    """
    def __init__(self, iter1, iter2, combiner):
        self.iter1 = iter(iter1)
        self.iter2 = iter(iter2)
        self.combiner = combiner
    
    def __next__(self):
        res = self.combiner(next(self.iter1), next(self.iter2))
        return res
    
    def __iter__(self):
        return self
        
class Fibonacci(object):
    """
    >>> fib = Fibonacci()
    >>> [next(fib) for _ in range(10)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    def __init__(self):
        self.first = 0
        self.second = 1
    
    def __next__(self):
        result = self.first
        self.first, self.second = self.second, self.first + self.second
        return result
    
    def __iter__(self):
        return self
        
def perfect_squares():
    """
    >>> sq = perfect_squares()
    >>> [next(sq) for _ in range(10)]
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    """
    x = 0
    while True:
        yield x * x
        x += 1
