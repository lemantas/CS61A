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
    >>> comb_iter = iter(comb)
    >>> next(comb_iter)
    0
    >>> next(comb_iter)
    2
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
