"""
This is just a simple user defined type - Vector
"""

import math

class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'Vector({0:self.x!r}, {1:self.y!r})'
    
    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))
    
    def __add__(self, other: "Vector") -> "Vector":
        x = self.x + other.x
        y = self.x + other.y
        return Vector(x, y)
    
    def __mul__(self, scalar: int) -> "Vector":
        return Vector(self.x * scalar , self.y * scalar)

