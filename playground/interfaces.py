class Vector:
    def __init__(self, vector):
        assert len(vector) >= 3, "Must be a list with at least 3 coordinates"
        self.vector = vector
        
    def __neg__(self):
        return Vector([-v for v in self.vector])
        
    def __add__(self, other):
        assert type(other) == Vector, "Invalid operation!"
        assert len(self) == len(other), "Invalid dimensions!"
        return Vector([x + y for x, y in zip(self.vector, other.vector)])
        
    def __sub__(self, other):
        return self.__add__(-other)
        
    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Vector([x * other for x in self.vector])
        elif type(other) == Vector:
            return Vector([x * y for x, y, in zip(self.vector, other.vector)])
        
    def __rmul__(self, other):
        return self.__mul__(other)
        
    def __len__(self):
        return len(self.vector)
        
    def __getitem__(self, n):
        return self.vector[n]
        
    def __str__(self):
        return "Vector({})".format([x for x in self.vector])
        
    def __repr__(self):
        return self.__str__()
