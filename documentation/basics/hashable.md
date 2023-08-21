# Hashable Objects

> An object is hashable if it has a hash code which never changes during its lifetime (it needs a `__hash__()` method), and can be compared to other objects (it needs an `__eq__()` method). Hashable objects which compare equal must have the same hash code.

## Hashable Types

1. `Numeric` types;
1. Flat immutable[^1] types `str` and `bytes`;
1. Container types[^1] if the object and all elements are immutable and hashable:
    - [`FrozenSet`](../data_structures/set.md#frozenset) are hashable because every element it contains must be hashable by definition;
    - A [`Tuple`](../data_structures/tuple.md) is hashable `only if all its items are hashable`;

[^1]: [Flat vs Container debate](../data_structures/sequence.md#container-x-flat)

## Characteristics

1. The `hash code might vary` based on the Python version, machine setup, and the way the hash was created;
1. The hase code is `guaranteed to be the same only within one Python process`;
1. `Custom user-defined types are hashable by default`. This happens because their hash code is derived from their `id()`, and the `__eq__()` method, which is inherited from the object class, simply checks whether the object IDs are the same;
1. If an `object implements a custom __eq__()` that takes into account its `internal state`, it will be hashable only if its `__hash__() always returns the same hash code`:
    - In practice, this requires that `__eq__()` and `__hash__()` only take into account instance attributes that never change during the life of the object

## Code

```pycon exec="1" source="console" title="hashable_obj.py"
>>> tt = (1, 2, (30, 40))
>>> print(hash(tt))
>>> tl = (1, 2, [30, 40])
>>> try:
...     hash(tl)
... except BaseException as ex:
...     print(f"Hash error when use unhashable obj: {ex}")
>>> tf = (1, 2, frozenset([30, 40]))
>>> print(hash(tf))
```

## References

- [Fluent Python, 2nd Edition](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/)
