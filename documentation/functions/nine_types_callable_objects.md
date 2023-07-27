# The Nine Types of Callable Objects

To determine whether an object is callable, use the `callable()` built-in function.

## User-Defined Functions

Created with `def` statements or `lambda` expressions;

## Built-in Functions

A function implemented in C (for CPython), like `len` or `time.strftime`.

## Built-in Methods

Methods implemented in C, like `dict.get`.

## Methods

Functions defined in the body of a class.

## Classes

When invoked, a class runs its `__new__` method to create an instance, then `__init__` to initialize it, and finally the instance is returned to the caller;

## Class instances

If a class defines a `__call__` method, then its instances may be invoked as functions;

## Generator Functions

Functions or methods that use the `yield` keyword in their body. When called, they return a generator object.

## Native Coroutine Functions

Functions or methods defined with `async def`. When called, they return a coroutine object.

## Asynchronous Generator Functions

Functions or methods defined with `async def` that have `yield` in their body. When called, they return an asynchronous generator for use with `async for`

## References

- [Fluent Python, 2nd Edition](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/)
