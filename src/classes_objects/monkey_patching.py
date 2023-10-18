class MyClass:
    def original_method(self):
        print("This is the original method.")

def new_method(self):
    print("Patched behavior")

obj = MyClass()
obj.original_method()
# Monkey patching the 'original_method' with 'new_method'
MyClass.original_method = new_method

# Calling the 'original_method' after monkey patching
obj.original_method()
