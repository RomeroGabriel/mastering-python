class Vector:
    __slots__ = ("x", "y")
    x: int
    y: int

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class BetterVector(Vector):
    ...

bv = BetterVector(1, 2)
print(bv.__dict__)
bv.name = "BetterVector"
print(bv.__dict__)