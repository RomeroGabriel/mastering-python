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

## Multiple Inheritance - Execution Order and MRO Attritube

`Inheritance is guided by a special class attribute named __mro__`, which stands for `Method Resolution Order`. This attribute `lists the class and its superclasses in the order that Python uses to search for methods`.

Any programming language implementing `multiple inheritance must address potential naming conflicts when superclasses implement a method with the same name`. This is known as the `diamond problem`. When superclasses have `conflicting method names`, the `execution call order follows the sequence in __mro__, which reflects the inheritance order during class definition`.

!!! example
    Consider the following scenario with two classes, `A and B, both of which are parent classes of a third class C`. Suppose there's a `method called ping() defined in all three classes`, and class `C calls super().method()` in its implementation.
    When the method is called on an instance of class C, `it would trigger the execution of the method in classes A and B in accordance with the Method Resolution Order (mro)`. However, if class `B's ping() does not include a call to super().ping(), the chain of method calls following the Method Resolution Order will stop at class B`, and the method in class A will not be invoked.

## Mixin Classes

`A mixin class is intended to be subclassed alongside at least one other class in a multiple inheritance structure`. A mixin should not be the sole base class of a concrete class, as it doesn't offer all the functionality for a concrete object. Instead, it augments or customizes the behavior of child or sibling classes.
