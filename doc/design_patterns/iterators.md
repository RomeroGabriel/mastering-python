# Iterators

Iteration is a fundamental aspect of data processing in which programs `apply computations to data series`. When dealing with `data that doesn't fit into memory`, the need arises to fetch `items lazily—one at a time and on demand`. This is precisely the role of an iterator.

In Python, `every standard collection is iterable`. `An iterable is an object that offers an iterator`, a mechanism Python utilizes to facilitate operations such as:

1. `for` loops
1. List, dict, and set comprehensions
1. Unpacking assignments
1. Construction of collection instances

## The iter Function

When Python needs to iterate over an object,  it automatically invokes `iter(object)`. The built-in `iter` function examines whether the `object implements __iter__` and calls it to acquire an iterator. In cases where `__iter__` is not implemented but `__getitem__` is present, `iter() generates an iterator attempting to retrieve items by index, starting from 0`. If this attempt fails, Python raises a `TypeError`, typically indicating that the object is not iterable.

This is the reason why `all Python sequences are iterable`; by definition, they all implement `__getitem__`. Notably, the standard sequences also implement `__iter__`, and it is advisable for your custom sequences to do the same. This is because iteration via `__getitem__ is maintained for backward compatibility` but may be deprecated in the future.

!!! warning "isinstance check and goose-typing"
    In the `goose-typing` approach, defining an iterable is more straightforward but less flexible: a`n object is deemed iterable if it implements the __iter__ method`.

```python
>>> class GooseSpam:
...     def __iter__(self):
...         pass
...
>>> from collections import abc
>>> issubclass(GooseSpam, abc.Iterable)
True
>>> goose_spam_can = GooseSpam()
>>> isinstance(goose_spam_can, abc.Iterable)
True
```

## Iterables vs Iterators

!!! info "Iterable"
    An iterable refers to `any object from which the iter built-in function can obtain an iterator`. `Objects that implement an __iter__ method returning an iterator are considered iterable`. Sequences, by definition, are always iterable. Objects implementing a `__getitem__` method that accepts 0-based indexes are also iterable.

!!! warning "Relationship Between Iterables and Iterators"
    `Python acquires iterators from iterables.`

!!! info "Python’s standard interface for an iterator"
    Two methods:
    1. `__next__`: Returns the next item in the series, raising `StopIteration` if there are no more.
    1. `__iter__`: Returns `self` and this `enables iterators to be used where an iterable is expected`, such as in a for loop.

`The StopIteration exception indicates that the iterator is exhausted`. Internally, this exception is managed by the iter() built-in, which is integral to the logic of for loops and other iteration contexts like list comprehensions and iterable unpacking.

This interface is formalized in the `collections.abc.Iterator` ABC (Abstract Base Class), which declares the abstract `__next__` method and subclasses Iterable—where the abstract `__iter__` method is declared.

!!! example
    ![The Iterable and Iterator ABCs. Methods in italic are abstract. from Fluent Python, 2nd Edition](https://raw.githubusercontent.com/RomeroGabriel/mastering-python/main/doc/images/design_patterns/uml-iterator.png)
    > The Iterable and Iterator ABCs. Methods in italic are abstract. from Fluent Python, 2nd Edition

Due to the minimal methods required for an iterator (`__next__` and `__iter__`), `checking for remaining items involves calling next() and catching StopIteration`. Additionally, it is not possible to reset an iterator. `If you need to start over, you must call iter() on the iterable that created the iterator initially`. This minimal interface is sensible, `as not all iterators are resettable`. For instance, if an iterator is reading packets from the network, there's no way to rewind it.
