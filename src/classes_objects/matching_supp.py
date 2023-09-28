class Vector:
    x: int
    y: int

    __match_args__ = ('x', 'y')

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Vector(x={self.x}, y={self.y})"
    
    def __repr__(self) -> str:
        return f"Vector(x={self.x}, y={self.y})"


def positional_pattern_demo(v: Vector):
    match v:
        case Vector(x=0, y=0):
            print(f'{v!r} is null')
        case Vector(x=0):
            print(f'{v!r} is vertical')
        case Vector(y=0):
            print(f'{v!r} is horizontal')
        case Vector(x=x, y=y) if x==y:
            print(f'{v!r} is diagonal')
        case _:
            print(f'{v!r} is awesome')

positional_pattern_demo(Vector(0, 0))
positional_pattern_demo(Vector(0, 2))
positional_pattern_demo(Vector(2, 0))
positional_pattern_demo(Vector(1, 1))
positional_pattern_demo(Vector(2, 11))
