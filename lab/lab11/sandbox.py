class IteratorA:
    def __init__(self):
        self.start = 5

    def __next__(self):
        if self.start == 100:
            raise StopIteration
        self.start += 5
        return self.start

    def __iter__(self):
        return self
        
class IteratorB:
    def __init__(self):
        self.start = 5

    def __iter__(self):
        return self

class IteratorC:
    def __init__(self):
        self.start = 5

    def __next__(self):
        if self.start == 10:
            raise StopIteration
        self.start += 1
        return self.start
        
class IteratorD:
    def __init__(self):
        self.start = 1

    def __next__(self):
        self.start += 1
        return self.start

    def __iter__(self):
        return self
        
        
t = IteratorA()
t = t.__iter__()
try:
    while True:
        print(t.__next__())
except StopIteration as e:
    pass
