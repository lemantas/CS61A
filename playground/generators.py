class Naturals():
    def __init__(self):
        self.current = 0
        
    def __next__(self):
        result = self.current
        self.current += 1
        return result
        
    def __iter__(self):
        return self
        
class IterCombiner(object):
    def __init__(self, iter1, iter2, combiner):
        self.iter1 = iter1
        self.iter2 = iter2
        self.combiner = combiner
    
    def __next__(self):
        yield self.combainer(next(self.iter1), next(self.iter2))
    
    def __iter__(self):
        return self
