# Data Model

With the Python Data Model, `user-defined types can mimic the behavior of built-in types seamlessly`. This can be achieved without relying on inheritance; instead, it follows the principle of `duck typing`: you only need to implement the necessary methods for your objects to behave as intended.

`Think of the data model as a description of Python as a framework: It formalizes interfaces for our objects to behave like standard Python data structures` such as sequences, iterators, coroutines, classes, context managers, and so on. The Python interpreter `invokes these special methods to perform basic object operations, often triggered by special syntax`. These special method names are always written with leading and trailing double underscores, and they are also referred to as `"dunder" methods`.

## Protocols and Duck Typing

With duck typing, `you don't need to inherit from any special class to create fully functional behaviors` like a sequence type in Python. `You just need to implement the methods that fulfill the sequence protocol`. In the context of object-oriented programming, a protocol is an informal interface defined only in documentation, not in code.

For instance, the `sequence protocol in Python requires only the __len__ and __getitem__ methods.` `Any class that implements these methods with the standard signature and semantics can be used wherever a sequence is expected`. Whether the class is a subclass of something else is irrelevant; `all that matters is that it provides the necessary methods.`

Since `protocols are informal and unenforced`, you can often implement `just part of a protocol`, especially if you `know the specific context where a class will be used`. For example, to support iteration, you only need to provide the `__getitem__` method; there's no need to include \__len__.

## Sequence Protocol

To create a class that can behave like a sequence in Python, you only need to implement two methods: `__len__` and `__getitem__`.

??? info "`__len__`"
    When a class implements `__len__`, you can use the `len()` function with instances of that class.

??? info "`__getitem__`"
    When a class implements `__getitem__`, you can `access items in it just like you would with regular Python collections.`

??? example

    ``` py title="src/data_model/sequence_protocol_basic.py"
    --8<-- "src/data_model/sequence_protocol_basic.py"
    ```

    ```bash title="output"
    len of v1: 5
    5
    3
    [1, 2]
    [2, 3, 4, 5]
    Is 5 in v1? True
    Is 15 in v1? False
    ```

### More Complete Sequence Protocol

To ensure that when an object is sliced, the `returned object is of the same type as the original object`, you need to implement a more comprehensive `__getitem__` method. This method should handle slicing and return an instance of the same class with the sliced elements.

??? example

    ``` py title="src/data_model/sequence_protocol_deep.py"
    --8<-- "src/data_model/sequence_protocol_deep.py"
    ```

    ```bash title="output"
    len of v1: 5
    5
    3
    Vector ([1, 2])
    <class '__main__.Vector'>
    Vector ([2, 3, 4, 5])
    <class '__main__.Vector'>
    ```

## Object Representations

Python offers two methods for obtaining a string representation from any object:

??? info "repr()"
    The `repr()` function in Python returns a string that represents an object as the developer intends to see it. `This is the string you typically see when the Python console or a debugger shows an object`.

??? info "str()"
    The `str()` function in Python returns a string that `represents an object as the user would like to see it`. `This is the string you typically get when you use the print() function to display an object`. It's designed to provide a more human-readable and user-friendly representation of the object.

The special methods `__repr__` and `__str__` support repr() and str(). If the `__str__` method is not implemented for an object, `Python will use the implementation inherited from the base object class`, which, in turn, calls the `__repr__` method as a fallback.

??? example

    ```pycon exec="1" source="console"
    >>> from array import array
    >>> class Vector:
    >>>     def __init__(self, x=0, y=0):
    ...         self.x = x
    ...         self.y = y
    >>>     def __repr__(self):
    ...         return f'Vector({self.x!r}, {self.y!r}) nice'
    >>>     def __str__(self):
    ...         return str(tuple([self.x, self.y]))
    >>> v1 = Vector(1, 2)
    >>> print(v1)
    >>> print(repr(v1))
    ```

### Alternative Representations

There are two additional special methods for supporting alternative representations of objects: `__bytes__` and `__format__`.

!!! info "`__bytes__`"
    This method is analogous to `__str__`. It is called by the `bytes() function` to obtain the object represented as a byte sequence.

!!! info "`__format__`"
    This method is `used by f-strings, the built-in format() function, and the str.format() method`.

## Formatted Displays

In Python, `f-strings, the format() function, and str.format()` method handle formatting by calling the ``.__format__(format_spec)` method of the respective data types. The `format_spec` is a formatting specifier, which can be either:

1. The second argument in `format(my_obj, format_spec)`.
1. Anything that comes after a colon inside a replacement field within curly braces `{} in an f-string` or the `fmt in fmt.str.format()`.

If a class doesn't have a `.__format__` method defined, it will inherit the behavior from the object class, which returns the string representation of the object using str(my_object).

??? example "Formatted Examples"

    ```pycon exec="1" source="console"
    >>> div_value = 24/9
    >>> print(f"div_value: {div_value}")
    >>> print(f"format by 0.4f: {format(div_value, '0.4f')}")
    >>> print("24/9 = {value:0.2f}".format(value=div_value))
    ```

??? example "Dunder `__format__` example"

    ```pycon exec="1" source="console"
    >>> class nice_class:
    ...     def __init__(self, str_value: str):
    ...         self.str_value = str_value
    ...     def __format__(self, fmt_spec=''):
    ...         formatter = ""
    ...         if fmt_spec.endswith("n"):
    ...             formatter = "NICE STRING "
    ...         return formatter + self.str_value
    >>> obj_nice = nice_class("nice_str")
    >>> print(format(obj_nice))
    >>> print(f"obj: {obj_nice}")
    >>> print(format(obj_nice, "n"))
    ```

## Supporting Positional Pattern Matching

For a class to support positional pattern matching, you need to add a `__match_args__` class attribute. This attribute should `list the instance attributes in the order they will be used during pattern matching`. It's important to note that `__match_args__ doesn't have to include all public instance attributes`. Typically, you include the required arguments from the `__init__` method in __match_args, `but optional arguments may be omitted`.

??? example "Matching Support"

    ``` py title="src/classes_objects/matching_supp.py"
    --8<-- "src/classes_objects/matching_supp.py"
    ```

    ```bash title="output"
    Vector(x=0, y=0) is null
    Vector(x=0, y=2) is vertical
    Vector(x=2, y=0) is horizontal
    Vector(x=1, y=1) is diagonal
    Vector(x=2, y=11) is awesome
    ```

## Operator Overloading

Operator overloading enables `user-defined objects` to work with infix operators like `+` and `|`, or unary operators such as `-` and `~`. In Python, a thoughtful balance is maintained between flexibility, usability, and safety by introducing certain constraints on operator overloading:

1. We cannot change the meaning of the operators for the `built-in types`.
1. We `cannot create new operators`, only overload existing ones.
1. A few operators can’t be overloaded: `is`, `and`, `or`, and `not`.

### Unary Operators (+, -, and ~)

!!! info "`-`, implemented by `__neg__`"
    Arithmetic unary negation. If `x` is -2 then `-x == 2`.

!!! info "`+`, implemented by `__pos__`"
    Arithmetic unary plus. Usually `x == +x`.

!!! info "`~`, implemented by `__invert__`"
    Bitwise not, or bitwise inverse of an integer, defined as `~x == -(x+1)`. If `x` is 2 then `~x == -3`.

To implement unary operators (+, -, and ~) for your class, you need to `define the appropriate special method that takes only one argument: self`.

!!! warning "Follow the General Rule for Operators"
    `Always return a new object`. This means do not changes the receiver `self` and instead creating and returning a new instance of a suitable type.
    For unary `-` and `+`, the result will likely be an `instance of the same class as self`. For unary `+`, if the receiver is `immutable`, you should return self; otherwise, return a copy of self.

??? example

    ``` py title="src/classes_objects/unary_operators.py"
    --8<-- "src/classes_objects/unary_operators.py"
    ```

    ```bash title="output"
    Initial Vector: Vector(x=2, y=1)
    Plus Vector: Vector(x=3, y=2)
    Negation Vector: Vector(x=-2, y=-1)
    Bitwise not Vector: Vector(x=-3, y=-2)
    FINAL Vector: Vector(x=2, y=1)
    ```

### Listing All Operators

| Operator        | Forward        | Reverse        | In-place       | Description                              |
| --------------- | -------------- | -------------- | -------------- | ---------------------------------------- |
| +               | `__add__`      | `__radd__`     | `__iadd__`     | Addition or concatenation                |
| -               | `__sub__`      | `__rsub__`     | `__isub__`     | Subtraction                              |
| *               | `__mul__`      | `__rmul__`     | `__imul__`     | Multiplication or repetition            |
| /               | `__truediv__`  | `__rtruediv__` | `__itruediv__` | True division                            |
| //              | `__floordiv__` | `__rfloordiv__`| `__ifloordiv__`| Floor division                           |
| %               | `__mod__`      | `__rmod__`     | `__imod__`     | Modulo                                   |
| divmod()        | `__divmod__`   | `__rdivmod__`  | `__idivmod__`  | Returns tuple of floor division quotient and modulo |
| **, pow()       | `__pow__`      | `__rpow__`     | `__ipow__`     | Exponentiation                           |
| @               | `__matmul__`   | `__rmatmul__`  | `__imatmul__`  | Matrix multiplication                    |
| &               | `__and__`      | `__rand__`     | `__iand__`     | Bitwise and                              |
| \|              | `__or__`       | `__ror__`      | `__ior__`      | Bitwise or                               |
| ^               | `__xor__`      | `__rxor__`     | `__ixor__`     | Bitwise xor                              |
| <<              | `__lshift__`   | `__rlshift__`  | `__ilshift__`  | Bitwise shift left                       |
| >>              | `__rshift__`   | `__rrshift__`  | `__irshift__`  | Bitwise shift right                      |

## References

- [Fluent Python, 2nd Edition](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/)
