# Classes

## Classmethod x Staticmethod

The `@classmethod` decorator: Method operating on the class, not instances. `Receives the class as its first argument, often used for alternative constructors`.

The `@staticmethod` decorator: `Method with no special first argument`. Functions like a regular function defined in a class, not dependent on class or instance. Typically used for class-related utility functions.

```pycon exec="1" source="console" title="class_static_example.py"
>>> class Test:
...     @classmethod
...     def class_test(*args):
...         print(args)
...     @staticmethod
...     def static_test(*args):
...         print(args)
>>> Test.class_test()
>>> Test.static_test()
>>> Test.class_test(123)
>>> Test.static_test(123)
```

### Private and Protected Attributes

In Python, `there are no true private variables`. Instead, Python provides a `mechanism to prevent accidental overwriting of private attributes in subclasses`.

This mechanism involves `naming an instance attribute with two leading underscores` (e.g., \__att). When you do this, Python internally stores the name in the instance's `__dict__`, but it's prefixed with a leading underscore and the class name. This mechanism is commonly referred to as `name mangling`.

It's essential to understand that `name mangling is more about safety than security`. `Its purpose is to prevent accidental access rather than to hide attributes completely`. For instance, they can use v1._Vector__x = 7. `However, it's generally considered bad practice to do this in production code`.

Python programmers conventionally `use a single underscore prefix` (e.g., _att) `for attributes that should not be accessed from outside the class`. This follows a strong convention within the Python community to respect the privacy of attributes marked with a single underscore.

## Using \__slots__

In Python, `instance attributes are usually stored in a dictionary called __dict__`, but `dict has a significant memory overhead`. To save memory, you can use a special attribute called `__slots__`. `By defining __slots__ in your class, you specify a fixed set of attribute names that will be stored more efficiently`.

Remember that __slots__ must be defined when `creating the class`, adding or changing it later has no effect. The attribute names may be in a tuple or list, but is `prefer a tuple to make it clear there’s no point in changing it`.

??? example "How and consequences using Slots"

    ``` py title="src/classes_objects/slots.py"
    --8<-- "src/classes_objects/slots.py"
    ```

    ```bash title="output"
    'Vector' object has no attribute '__dict__'
    1
    2
    'Vector' object has no attribute 'name'
    ```

### Inheritance with \__slots__

`The effect of \__slots__ is partially inherited by a subclass`. . To ensure that instances of a subclass have no \__dict__, `you must declare __slots__ again in the subclass`. Essentially, the __slots__ of the superclass are combined with the __slots__ of the current class.

If you declare `\__slots__ = () (an empty tuple)` in the subclass, instances of the subclass will have no \__dict__ and will only accept attributes specified in the \__slots__ of the base class.

??? example

    ``` py title="src/classes_objects/slots_inheritance.py"
    --8<-- "src/classes_objects/slots_inheritance.py"
    ```

    ```bash title="output"
    {}
    {'name': 'BetterVector'}
    ```

### Issues with \__slots__

1. Remember to declare \__slots__ in each subclass to prevent instances from having \__dict__.
1. Classes using \__slots__ `cannot use the @cached_property decorator, unless they explicitly name __dict__ in __slots__`.
1. `Instances cannot be targets of weak references, unless you add __weakref__ in \__slots__`.

## References

- [Fluent Python, 2nd Edition](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/)
- [mCoding - Python \__slots__ and object layout explained](https://www.youtube.com/watch?v=Iwf17zsDAnY)
