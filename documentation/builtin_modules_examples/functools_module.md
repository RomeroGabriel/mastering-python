# Functools Module

The `functools` module provides several higher-order functions.

## functools.cache

> Python >= 3.9, Python < 3.9 use [lru_cache](#functoolslru_cache)

Related with:

- [Decorators](../decorators_closures/decorators.md)

`Implements memoization`, which is an optimization technique that `saves the results of previous invocations of an expensive function`. This `avoids redundant computations when the function is called with the same arguments again`.

`All the arguments taken by the decorated function must be hashable`. To save the results of previous calls, a dictionary object is used, where the keys are generated from the positional and keyword arguments used in the calls.

`Really good in applications that need to fetch information from remote APIs.`

```python title="cache.py"
>>> from functools import cache
>>> @cache
>>> def fibonacci(n):
...     if n < 2:
...         return n
...     return fibonacci(n - 2) + fibonacci(n - 1)
```

## functools.lru_cache

The main advantage of lru_cache compared to [cache](#functoolscache) is that `lru_cache will retain at most 128 entries at any given time`. The acronym LRU stands for Least Recently Used, indicating that `older entries that haven't been accessed for a while are removed to create space for new ones`.

```python title="lru_cache.py"
>>> from functools import cache
>>> @lru_cache
>>> def fibonacci(n):
...     if n < 2:
...         return n
...     return fibonacci(n - 2) + fibonacci(n - 1)
```

## functools.singledispatch

In brief, it's a decorator used to `establish polymorphism/overloaded functions`. It permits various modules to contribute to the overall solution and enables you to easily `supply specialized functions, even for types from third-party packages that you can't modify`. The function adorned with `@singledispatch` serves as the entry point for a generic function.

`The function that gets executed depends on the type of the first argument` provided at runtime. The `names of the specialized functions don't matter`; using `_` is a good choice to make this clear.  `If you can't or don't want to add type hints to the decorated function, you can pass a type to the @«base».register decorator.`

`Whenever possible, register specialized functions to handle Abstract Base Classes (ABCs)` like numbers.Integral and abc.MutableSequence. This allows your code to support a wider range of compatible types.

An important feature of the singledispatch mechanism is that `you can register specialized functions anywhere in your system, in any module`. You can create custom functions for classes you didn't write and can't modify.

```pycon exec="1" source="console" title="singledispatch.py"
>>> from functools import singledispatch
... ...
>>> @singledispatch
>>> def nice_add(num1: int, num2: int):
...     print("INT DEFAULT nice_add")
...     return num1 + num2
... ...
>>> @nice_add.register
>>> def _(num1: float, num2: float):
...     print("FLOAT nice_add")
...     return num1 + num2
... ...
>>> @nice_add.register(str)
>>> def _(num1, num2):
...     print("STRING nice_add")
...     return int(num1) + int(num2)
... ...
>>> nice_add(1, 2)
>>> nice_add(1.2, 2.5)
>>> nice_add("1", "2")
```

## functools.partial

Given a callable, it produces a new callable with some of the arguments of the original `callable bound to predetermined values`. `partial` takes a callable as first argument, followed by an arbitrary number of positional and keyword arguments to bind. The `functools.partialmethod` function does the same job as partial, but is designed to work with `methods`.

```pycon exec="1" source="console" title="lambda.py"
>>> from operator import mul
>>> from functools import partial
>>> triple = partial(mul, 3)
>>> print(triple(7))
>>> result = list(map(triple, range(1, 10)))
>>> print(result)
```

## References

- [Fluent Python, 2nd Edition](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/)
- [Functools — Higher-order functions and operations on callable objects](https://docs.python.org/3/library/functools.html)
