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
