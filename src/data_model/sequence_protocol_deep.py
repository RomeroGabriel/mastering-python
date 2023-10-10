class Vector:
    pointers: list[int]

    def __init__(self, pointers: list[int]):
        self.pointers = pointers

    def __repr__(self) -> str:
        return f"Vector ({self.pointers})"

    def __len__(self):
        return len(self.pointers)
    
    def __getitem__(self, index):
        if isinstance(index, slice):
            cls = type(self)
            return cls(self.pointers[index])
        return self.pointers[index]
    

v1 = Vector([1, 2, 3, 4, 5])
print(f"len of v1: {len(v1)}")

print(v1[-1])
print(v1[2])
print(v1[:2])
print(type(v1[:2]))
print(v1[1:])
print(type(v1[1:]))