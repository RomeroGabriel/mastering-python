class Vector:
    pointers: list[int]

    def __init__(self, pointers: list[int]):
        self.pointers = pointers

    def __len__(self):
        return len(self.pointers)
    
    def __getitem__(self, index):
        return self.pointers[index]
    

v1 = Vector([1, 2, 3, 4, 5])
print(f"len of v1: {len(v1)}")

print(v1[-1])
print(v1[2])
print(v1[:2])
print(v1[1:])
print(f"Is 5 in v1? {5 in v1}")
print(f"Is 15 in v1? {15 in v1}")