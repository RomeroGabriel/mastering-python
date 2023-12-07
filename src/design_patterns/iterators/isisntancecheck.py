class Test:
    def __iter__(self):
        pass    

from collections import abc

print(f"Class Test is an Iterable subclass? {issubclass(Test, abc.Iterable)}")
test_var = Test()
print(f"test_var instance Test is an Iterable instance? {isinstance(test_var, abc.Iterable)}")