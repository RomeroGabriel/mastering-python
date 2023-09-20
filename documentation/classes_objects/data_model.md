# Data Model

With the Python Data Model, `user-defined types can mimic the behavior of built-in types seamlessly`. This can be achieved without relying on inheritance; instead, it follows the principle of `duck typing`: you only need to implement the necessary methods for your objects to behave as intended.

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

## References

- [Fluent Python, 2nd Edition](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/)
