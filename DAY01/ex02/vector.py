import numpy


class Vector:
    '''"In this exercise, you have to create a Vector class.
The goal is to have vectors and be able to perform mathematical operations
with them.'''
    def __init__(self, values):
        self.values = values
        if isinstance(values, tuple) and len(values) == 2:
            self.values = range(values[0], values[1])
        elif isinstance(values, int):
            self.values = range(values)
        self.values = tuple([float(i) for i in self.values])
        self.size = len(self.values)

    def __add__(self, other):
        """ Returns the vector addition of self and other """
        if len(self.values) != len(other.values):
            raise IndexError('Vectors must have same dimmensions.')
        else:
            added = (a + b for a, b in zip(self.values, other.values))
            return Vector(added)

    def __radd__(self, other):
        # add : scalars and vectors, can have errors with vectors.
        added = (a + other for a in self.values)
        return Vector(added)

    def __sub__(self, other):
        pass

    def __rsub__(self, other):
        # sub : scalars and vectors, can have errors with vectors.
        pass

    def __truediv__(self, other):
        pass

    def __rtruediv__(self, other):
        # div : only scalars.
        pass

    def __mul__(self, other):
        pass

    def __rmul__(self, other):
        # mul : scalars and vectors, can have errors with vectors,
        # return a scalar if we perform Vector * Vector (dot product)
        pass

    def __str__(self):
        return ('(Vector ' + str(list(self.values)) + ')')
    
    def __repr__(self):
        return ('(Vector ' + list(self.values) + ')')


V3 = Vector([6.0, 8.0, 5.0, 5])
V4 = Vector(4)
V5 = Vector((10, 14))
print(V3)
print(V4)
print(V5)
V1 = V3 + V4 + V5
print(V1)
print(V3.__radd__(3))
