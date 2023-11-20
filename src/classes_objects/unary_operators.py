class Vector:
    x: int
    y: int

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Vector(x={self.x}, y={self.y})"
    
    def __repr__(self) -> str:
        return f"Vector(x={self.x}, y={self.y})"

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __pos__(self):
        return Vector(self.x + 1, self.y + 1)
    
    def __invert__(self):
        return Vector(-(self.x + 1), -(self.y + 1))
    
vec = Vector(2, 1)
print(f"Initial Vector: {vec}")
print(f"Plus Vector: {+vec}")
print(f"Negation Vector: {-vec}")
print(f"Bitwise not Vector: {~vec}")
print(f"FINAL Vector: {vec}")