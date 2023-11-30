# Tuple

A set is a built-in data structure in Python and is classified as a type of [sequence data structure](sequence.md).

## Characteristics

1. [Immutable Sequence](sequence.md#mutable-x-immutable)
1. [Container Sequence](sequence.md#container-x-flat)
1. Can be used as record
1. Just the tuple object is immutable, the tuple's element can change.
1. Use parentheses ()
1. Usually contain a heterogeneous sequence

## The Tuples references to Mutable Objects

Basic concepts:

1. [Object References](/documentation/basics/object_handling.md)

The concept of `immutability in tuples specifically pertains to the tuple's references`. It's crucial to note that while tuples themselves are immutable, this `immutability does not extend to the mutable objects they may reference`. Care should be taken when dealing with tuples containing mutable items to avoid potential sources of bugs.

```pycon exec="1" source="console" title="tuple_refs.py"
>>> a = (10, 'alpha', [1, 2])
>>> b = (10, 'alpha', [1, 2])
>>> print(f"a == b? {a == b}, A type = {type(a)} and B type = {type(b)}")
>>> b[-1].append(99)
>>> print(f"a == b? {a == b}")
>>> print(f"A now: {a} vs B now: {b}")
```

## Tuples as Records

If you are `familiar with the structure` of tuple objects, you can utilize tuples as record data, with each `item in the tuple representing data for a specific field`. The sequence of items holds significance, and the count of fields remains constant.

```pycon exec="1" source="console" title="tuple_as_records.py"
>>> countries_nationality = [('Chile', 'Chilean'), ('Brazil', 'Brazilian'), ('Argentina', 'Argentine'), ('Uruguay', 'Uruguayan')]
>>> for country, nationality in countries_nationality:
...     print(f"Country field: {country}, Nationality: {nationality}")
```

## Tuples vs Lists

Using Tuples instead of Lists can bring both `performance benefits and clarity` to your code:

1. Clarity: When you encounter a tuple in the code, you can be certain that its `length will remain constant`.
1. Performance: `Tuples consume less memory` compared to a list of equivalent length, enabling Python to implement optimizations.

A deeper discussion can be found here in this StackOverflow answer by Python core developer Raymond Hettinger

A deeper discussion can be found here in this [StackOverflow answer](https://stackoverflow.com/questions/68630/are-tuples-more-efficient-than-lists-in-python/22140115#22140115) provided by Raymond Hettinger, a Python core developer.

## Named Tuples

Named tuples in Python offer a way to `create tuples that enable you to access values using descriptive field names and the dot notation`, instead of relying on ambiguous integer indices.

### collections.namedtuple

Python's `namedtuple()` resides within the `collections` module as a factory function. It empowers you to generate `subclasses of tuples`, complete with named fields. This offers supplementary methods and attributes like `._make()`, `_asdict()`, and .`_fields`, among others. Notably, named tuples `maintain backward compatibility` with conventional tuples while `exhibiting comparable memory usage`.

```pycon exec="1" source="console" title="named_tuple_collections.py"
>>> from collections import namedtuple
>>> Point = namedtuple("Point", "x y")
>>> print(f"Is subclass of tuple? {issubclass(Point, tuple)}")
>>> point = Point(2, 4)
>>> print(point, point.x, point.y)
>>> print(point, point[0], point[1])
```

For further customization, including required and optional arguments, along with other details, see the the [Real Python article](https://realpython.com/python-namedtuple/).

### typing.NamedTuple

Within the `typing` module, there exists `NamedTuple`, a typed variant of namedtuple. This allows to craft namedtuple classes with `type annotations`. Notably, `both namedtuple and NamedTuple instances exhibit identical memory consumption characteristics`.

```pycon exec="1" source="console" title="named_tuple_typing.py"
>>> from typing import NamedTuple
>>> class Person(NamedTuple):
...     name: str
...     age: int
...     country: str = "Canada"
...
```

## References

- [Fluent Python, 2nd Edition](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/)
- [Python - Tuples and Sequences](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- [Real Python - Write Pythonic and Clean Code With namedtuple](https://realpython.com/python-namedtuple/)
