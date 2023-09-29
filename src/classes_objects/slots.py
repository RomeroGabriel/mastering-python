class Vector:
    __slots__ = ("x", "y")
    x: int
    y: int

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

v = Vector(1, 2)
try:
    print(v.__dict__)
except BaseException as ex:
    print(ex)

print(v.x)
print(v.y)
try:
    v.name = "NICE VECTOR"
except BaseException as ex:
    print(ex)
