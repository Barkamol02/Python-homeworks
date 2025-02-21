import math

class Vector:
    def __init__(self, *components):
        self.components = tuple(components)
    
    def __repr__(self):
        return f"Vector{self.components}"
    
    def __add__(self, other):
        if not isinstance(other, Vector) or len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions")
        return Vector(*(a + b for a, b in zip(self.components, other.components)))
    
    def __sub__(self, other):
        if not isinstance(other, Vector) or len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions")
        return Vector(*(a - b for a, b in zip(self.components, other.components)))
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(*(a * other for a in self.components))
        elif isinstance(other, Vector) and len(self.components) == len(other.components):
            return sum(a * b for a, b in zip(self.components, other.components))
        else:
            raise TypeError("Multiplication requires a scalar or another vector of the same dimension")
    
    def __rmul__(self, scalar):
        return self * scalar
    
    def magnitude(self):
        return math.sqrt(sum(a ** 2 for a in self.components))
    
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector")
        return self * (1 / mag)
    
    def __eq__(self, other):
        return isinstance(other, Vector) and self.components == other.components


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1) 
print(v1 + v2)  
print(v2 - v1)  
print(v1 * v2)  
print(3 * v1)  
print(v1.magnitude())  
print(v1.normalize())  
