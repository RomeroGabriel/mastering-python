# Dictionaries

A dict is a built-in data structure in Python.

## Characteristics

1. [Mutable Sequence](sequence.md#mutable-x-immutable)
1. Implemented using a hash table, highly optimized

## Dict Comprehensions

A dictcomp (dict comprehension) build a dict instance by taking key:value pairs from any iterable.

```pycon exec="1" source="console" title="dict_compre.py"
>>> dial_codes = [
...     (880, 'Bangladesh'),
...     (55,  'Brazil'),
...     (86,  'China'),
...     (91,  'India'),
... ]
>>> dict_country = { country: code 
...    for code, country in dial_codes }
>>> print(dict_country)
```

## Unpacking Mappings

Similar to [sequence unpacking](sequence.md#unpacking), you can `extract elements from a dictionary by using the * operator`. When you use a `single *, only the key` is returned, but when you `use **, both the key and the value` are returned.

```pycon exec="1" source="console" title="dict_unpack.py"
>>> def dump(*args,**kwargs):
...     print(f"args: {args} => just X, since we just unpack the key")
...     print(f"kwargs: {kwargs}")
>>> dump(*{'x': 1}, y=2, **{'z': 3})
```

## Merging Mappings

> Python 3.9 and above.

You can `merge mappings using | and |=`, which are also used as set union operators. The `| operator creates a new dictionary`, while the `|= operator updates an existing mapping in place`.

```pycon exec="1" source="console" title="merge_maps.py"
>>> d1 = {'a': 1, 'b': 3}
>>> d2 = {'a': 2, 'b': 4, 'c': 6}
>>> merged_dicts = d1 | d2
>>> print(f"merged_dicts => {merged_dicts} ============ d1 = {d1} and d2 {d2}")
>>> print("ATTENTION: Please note that, in cases where keys have the same values, the values from d2 (on the right side of the operation) have been retained.")
>>> print("--------------------------")
>>> d1 |= d2
>>> print(f"d1 = {d1} and d2 {d2}. Now d1 was updated")
```

## Patterns Matching

## Getting, Inserting or Updating

## References

- [Fluent Python, 2nd Edition](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/)
