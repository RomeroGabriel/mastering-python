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

<!-- TO DO -->