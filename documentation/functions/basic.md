# Basic of Functions

## Definitions and Arguments

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

## Polymorphism/overloaded Functions

!!! info "functools.singledispatch"
    Checkout functools.singledispatch section to see other use case. `functools.singledispatch is used for single-dispatch generic functions`.

This decorator is used in Python for `function overloading`. `It allows you to define multiple methods with the same name but different signatures`, enabling more flexible use. When used in conjunction with type hints, it helps improve the clarity and maintainability of code.

??? example

    ``` py title="src/functions/overload.py"
    --8<-- "src/functions/overload.py"
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

## The Nine Types of Callable Objects

To determine whether an object is callable, use the `callable()` built-in function.

### User-Defined Functions

Created with `def` statements or `lambda` expressions;

### Built-in Functions

A function implemented in C (for CPython), like `len` or `time.strftime`.

### Built-in Methods

Methods implemented in C, like `dict.get`.

### Methods

Functions defined in the body of a class.

### Classes

When invoked, a class runs its `__new__` method to create an instance, then `__init__` to initialize it, and finally the instance is returned to the caller;

### Class instances

If a class defines a `__call__` method, then its instances may be invoked as functions;

### Generator Functions

Functions or methods that use the `yield` keyword in their body. When called, they return a generator object.

### Native Coroutine Functions

Functions or methods defined with `async def`. When called, they return a coroutine object.

### Asynchronous Generator Functions

Functions or methods defined with `async def` that have `yield` in their body. When called, they return an asynchronous generator for use with `async for`

## References

- [Python - 4.7. Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Fluent Python, 2nd Edition](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/)
