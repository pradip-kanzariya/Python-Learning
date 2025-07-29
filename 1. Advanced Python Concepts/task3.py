# 1. Advanced Python Concepts

# Practice Task : 3 | Implement a class Vector that supports addition, subtraction, and string representation using dunder methods.
class Vector:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def __add__(self):
        result = [x+y for x, y in zip(self.v1, self.v2)]
        return f"Addition of v1 and v2 : {result}"
    
    def __sub__(self):
        result = [x-y for x, y in zip(self.v1, self.v2)]
        return f"Subtraction of v1 and v2 : {result}"
    
    def __str__(self):
        return f"v1 : {self.v1} and v2 {self.v2}"

v = Vector([1, 2, 3], [4, 5, 6])
print(v)
print(v.__add__())
print(v.__sub__())


# Practice Task : 3.1 | Implement a class Vector that supports addition, subtraction, and string representation using dunder methods.
class Vector:
    def __init__(self, elements):
        self.elements = elements

    def __add__(self, other):
        return list(map(lambda x, y : x + y, self.elements, other.elements))
    
    def __sub__(self, other):
        return list(map(lambda x, y : x - y, self.elements, other.elements))
    
    def __str__(self):
        return f"Vector : {self.elements}"
    
v1 = Vector([1,2])
v2 = Vector([3,4])
v3 = v1 + v2
print(f"v3 = {v3}")
v4 = v2 - v1
print(f"v4 = {v4}")
v5 = Vector(v4)
v6 = v5 - v1
print(f"v6 = {v6}")
