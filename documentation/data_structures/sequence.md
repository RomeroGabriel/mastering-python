# Built-In Sequences

Python provides various built-in sequence types implemented in C, offering a rich set of functionalities through their APIs. These sequences include lists, tuples, strings, and range objects, each with its own unique features and use cases.

## Classifications/Types of Sequences

### Container x Flat

Container sequences, such as lists, tuples, and collections.deque, `can hold items of different types`, including other nested containers. They `hold references to the objects they contain`, which may be of any type.

On the other hand, flat sequences, like str, bytes, and array.array, `hold items of one simple type and store the value of their contents in their own memory space`, not as separate Python objects. Refer to the image below for more details.

![Container x Flat. Image from Fluent Python, 2nd Edition](https://raw.githubusercontent.com/RomeroGabriel/mastering-python/main/documentation/images/data_structures/containerVSflat.png)
> Container x Flat. Image from Fluent Python, 2nd Edition

### Mutable x Immutable

Mutable sequences include list, bytearray, array.array, and collections.deque. These sequences `can be modified after creation`, allowing you to add, remove, or modify elements.

Immutable sequences include tuple, str, and bytes. Once created, these sequences `cannot be changed`, meaning their elements cannot be modified or added.

`Mutable sequences inherit all methods from immutable sequences` and also implement several additional methods. Refer to the image below for more details.

![Mutable Inherit. Image from Fluent Python, 2nd Edition](https://raw.githubusercontent.com/RomeroGabriel/mastering-python/main/documentation/images/data_structures/mutable_inherit.png)
> Mutable Inherit. Image from Fluent Python, 2nd Edition

## Unpacking

Sequence unpacking in Python allows you to `extract elements from a sequence without using indexes`. It avoids unnecessary and error-prone index-based extraction. This feature `works with any iterable object`, including iterators that don't support index notation (using []). Instead of accessing elements by index, you can assign them directly to variables using unpacking.

### Parallel assignment

The most visible form of unpacking, assigning items from an iterable to tuple of variable.

```pycon exec="1" source="console" title="unpacking_parallel_assignment.py"
>>> point = (123, 456)
>>> x, y = point
>>> print(f"X: {x}")
>>> print(f"Y: {y}")
```

```pycon exec="1" source="console" title="swapping_var_values.py"
>>> a = 10
>>> b = 15
>>> b, a = a, b
>>> print(f"A: {a}, B: {b}")
```

### Using *

Use the `*` prefix when calling a function to perform `unpacking of elements from a sequence`. It allows you to pass `multiple arguments from a sequence as individual arguments` to the function.

```pycon exec="1" source="console" title="unpacking_multiple_sequence.py"
>>> data = (20, 8)
>>> quotient, remainder = divmod(*data)
>>> print(quotient, remainder)
```

Using `*` to grab excess items

```pycon exec="1" source="console" title="excess_items_unpacking.py"
>>> a, b, *rest = range(5)
>>> print("REST ITEMS")
>>> print(f"WITH 5 => A: {a}, B: {b}, REST: {rest}")
>>> a, b, *rest = range(3)
>>> print(f"WITH 3 => A: {a}, B: {b}, REST: {rest}")
>>> a, b, *rest = range(2)
>>> print(f"WITH 2 => A: {a}, B: {b}, REST: {rest}")
>>> print()

>>> a, *body, c, d = range(5)
>>> print("MIDDLE ITEMS")
>>> print(f"A: {a}, BODY: {body}, C: {c}, D: {d}")
>>> *head, b, c, d = range(5)
>>> print(f"HEAD: {head}, B: {b}, C: {c}, D: {d}")
>>> print()

>>> print("In Function Calls")
>>> def fun(a, b, c, d, *rest):
...     return a, b, c, d, rest
>>> print(fun(*[1, 2], 3, *range(4, 7)))
>>> print()

>>> print("When defining list, tuple or set")
>>> print(*range(4), 4)
>>> print([*range(4), 4])
>>> print({*range(4), 4, *(5, 6, 7)})
```

### With function's return

You can use unpacking from function returns to allow functions to `return multiple values` conveniently. The caller can easily unpack the values into separate variables.

```pycon exec="1" source="console" title="swapping_var_values.py"
>>> import os
>>> # doesn't work with strings
>>> raw_return = os.path.split('/home/aws_nice_cluster/.ssh/id_rsa.pub') 
>>> print(f"raw_return: {raw_return}, type: {type(raw_return)}")
>>> _, filename = raw_return
>>> print(filename)
```

### Nested Unpacking

```pycon exec="1" source="console" title="swapping_var_values.py"
>>> metro_areas = [
...    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),  
...    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
...    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
...    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
...    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
... ]
>>> print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
>>> for name, _, _, (lat, lon) in metro_areas:  
...     if lon <= 0:  
...         print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')
```

## Pattern Matching

> Available in Python 3.10 and above!

In Python's pattern matching, the `subject` is the data following the `match` keyword, which Python aims to `match with patterns in each case clause`.  One key improvement of match over switch is `destructuring` - a more advanced form of unpacking the subject. A case clause has two parts: a `pattern` and an `optional guard with the if keyword`.

For subject `sequence pattern` matching, the following is necessary:

1. The subject  is a sequence;
1. The subject and the pattern have the same number of items and;
1. Each corresponding item matches, including nested items.

```pycon exec="1" source="console" title="sequence_matching_basic.py"
>>> def demonstration(self, message_type: list[str]) -> str:
...     match message_type: # message_type is the SUBJECT
...         case ['AAAA', 'BBB', 'CCC']:
...             return 'ABC'
...         case ['BBB', 'CCC']:
...             return 'BC'
...         case ['CCC']:
...             return 'C'
...         case _:
...             return ''
```

```pycon exec="1" source="console" title="sequence_matching_complex.py"
>>> metro_areas = [
...     ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
...     ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
...     ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
...     ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
...     ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
... ]
>>> print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
>>> for record in metro_areas:
>>>     match record:  
>>>         case [name, _, _, (lat, lon)] if lon <= 0: # using IF on case clause
>>>             print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')
```

### Special Treatment

1. In sequence patterns, `both square brackets and parentheses have the same significance`;
1. Cannot match sequences of type `str`, `bytes` and `bytearray`:
    1. A match subject of those types is `treated as an atomic value`;
    1. To treat as a sequence, `convert it in the match clause`;

    ```pycon exec="1" source="console" title="convert_str_match.py"
    >>> def phone_location(phone: str):
    >>>     match tuple(phone):
    ...         case ['1', *rest]:  # North America and Caribbean
    ...             return 1
    ...         case ['2', *rest]:  # Africa and some territories
    ...             return 2
    ...         case ['3' | '4', *rest]:  # Europe
    ...             return 3
    ```

1. The `_` symbol: it matches any single item in that position, but it is never bound to the value to the match item:
    1. Also, the only variable that `can appear more than once`

    ```python title="using_.py"
    # ['Shanghai', 'CN', 24.9, (31.1, 121.3)]
    case [name, _, _, (lat, lon) as coord]: 
    # name = Shanghai
    # lat = 31.1
    # lon = 121.3
    # coord = (31.1, 121.3)
    ```

## Generator Expressions

Generator expressions (gen-expr) are employed to `construct sequences`.  They `save memory by yielding items one by one` via the iterator protocol, unlike listcomps, which builds an entire list before feeding another constructor. Generator expressions share the same syntax as listcomps but `use parentheses` instead of brackets.

```pycon exec="1" source="console" title="gen_enx.py"
>>> symbols = '$¢£¥€¤'
>>> order_symbols = tuple(ord(symbol) for symbol in symbols)
>>> print(order_symbols)
>>> string_int = "12345"
>>> raw_gen = (value for value in string_int) 
>>> print(type(raw_gen))
>>> print(set(raw_gen))
```

## Examples

First case:

1. The first item must be an instance of `str`;
1. Item 3 must be a `pair of floats`.

```python title="match_by_type.py"
case [str(name), _, _, (float(lat), float(lon))]:
```

Second case:

1. Match any subject sequence `starting with a str`
2. Ending with a `nested sequence of two floats`

```python title="match_by_type.py"
case [str(name), *_, (float(lat), float(lon))]:
```

- The `*_` matches any number of items, `without binding them to a variable`;
- Using `*extra` instead of *_ would bind the items to `extra as a list` with 0 or more items.
