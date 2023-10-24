# Inheritance

!!! warning
    There's a `considerable pushback` against excessive inheritance usage in general, not just multiple inheritance, `due to the tight coupling of superclasses and subclasses`. Tight coupling implies that modifications in one segment of the program might result in unforeseen and widespread impacts in other areas, rendering systems fragile and difficult to comprehend. `Use with caution when using inheritance`.

## The super() Function

When a `subclass redefines a method of a superclass, it often needs to invoke the corresponding method of the superclass`. Calling an `overridden init` method is especially crucial to `enable superclasses to contribute to the initialization of the instance`.

```python
def __init__(self, a, b) :
    super().__init__(a, b)
    ...  # more initialization code
```

## Subclassing Built-In Types - DANGER

Typically, the code for `built-in types (written in C) doesn't usually invoke methods overridden by user-defined classes`. Directly subclassing built-in types such as `dict, list, or str` can be risky as the built-in methods often disregard user-defined overrides. Instead of subclassing the built-ins, it's advisable to derive your classes from the `collections module using UserDict, UserList, and UserString, which are intended for seamless extensions`.
