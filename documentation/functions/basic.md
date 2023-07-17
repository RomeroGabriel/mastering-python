# Basic of Functions

<!-- https://docs.python.org/3/tutorial/controlflow.html#defining-functions -->
## Definitions

The `def` keyword introduces a function definition, followed by the function name and a list of formal parameters enclosed in parentheses. The function body starts on the next line and must be indented.

When a function is called, the actual parameters (arguments) are introduced into the local symbol table of the called function. This is done using "*call by value*," where the **value passed is always an object reference, not the value of the object itself**. If a function calls another function or itself recursively, a new local symbol table is created for that call.

```pycon exec="1" source="console" title="fun_definition.py"

>>> def add_number(num1: int, num2: int) -> int:
...     # typing arguments and return are optional
...     return num1 + num2
```

Functions that belong to a class require the first argument to be `self`, which is used to pass the object reference to the function. This enables access to the class's attributes and methods within the function's body.

```pycon exec="1" source="console" title="fun_class.py"
>>> class Nice:
...     ...
>>>     def nice_func(self):
...         print("Nice object func starting with self")
```

## Return

Functions in Python can indeed **return multiple values**. When a function is called, it can produce multiple results. This capability allows functions to provide comprehensive information or results that can be used further in the code.

```pycon exec="1" source="console" title="mult_return.py"

>>> def add_sub_numbers(num1: int, num2: int) -> tuple[int, int]:
...     return num1 + num2, num1 - num2

>>> print(add_sub_numbers(2, 2))
```

Moreover, *even functions that do not explicitly contain a return statement still return a value*, albeit a default and unexciting one called `None`. When the return statement is missing, the interpreter automatically returns `None` as the function's output.

```pycon exec="1" source="console" title="fun_none.py"

>>> def add_number_print(num1: int, num2: int):
...     print(num1 + num2)

>>> print(add_number_print(2, 2))
```

## References

- [Python - 4.7. Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
