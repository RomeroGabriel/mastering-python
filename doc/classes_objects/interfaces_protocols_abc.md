# Interfaces, Protocols, and ABCs

The concept of interfaces in programming languages can be approached in various ways, depending on the language's features and design principles. Since Python 3.8, these are approaches present on the language:

!!! info "Duck typing"
    Python has been using this approach as its default typing method from the start. `It allows for determining the suitability of an object for a particular role based on its method and property set, rather than its type`.

!!! info "Goose typing"
    `Abstract base classes` (ABCs) in Python, introduced since version 2.6, employ this approach, `conducting runtime checks of objects against ABCs to determine their suitability for specific roles`.

!!! info "Static typing"
    Typically seen in statically-typed languages like C and Java, this approach has been supported in Python since version 3.5 through the `typing module`. `It is enforced by external type checkers` conforming to [PEP 484 (Type Hints)](https://peps.python.org/pep-0484/).

!!! info "Static duck typing"
    Inspired by the Go language, Python introduced support for this approach in version 3.8 through `subclasses of typing.Protocol`. `Similar to static typing, it is enforced by external type checkers`.

## The Typing Map

The four typing approaches depicted in the image are complementary: they have different pros and cons. It doesn’t make sense to dismiss any of them. Each of these four approaches rely on interfaces to work, but static typing can be done—poorly—using only concrete types instead of interface abstractions like protocols and abstract base classes.

!!! quote ""
    ![Typing Map. Image from Fluent Python, 2nd Edition](https://raw.githubusercontent.com/RomeroGabriel/mastering-python/main/doc/images/classes_objects/typing_map.png)
    [Typing Map. Image from Fluent Python, 2nd Edition](https://raw.githubusercontent.com/RomeroGabriel/mastering-python/main/doc/images/classes_objects/typing_map.png)

## Duck and Static Duck Typing

In Python, the concept of a `protocol refers to an informal interface`. With the integration of [PEP 544—Protocols: Structural subtyping (static duck typing)](https://peps.python.org/pep-0544/) in Python 3.8, the `term protocol has acquired an additional`, closely related yet distinct, meaning in the context of Python. `This PEP enables the creation of subclasses of typing.Protocol to define one or more methods that a class must implement or inherit to satisfy a static type checker`.

!!! info "Dynamic Protocol"
    `Refers to the implicit and convention-based protocols that have always existed in Python`. These protocols are [described in the documentation](https://docs.python.org/3/reference/datamodel.html) and are integral to the Python language. They are fundamentally flexible, allowing objects to implement only a portion of the protocol while still retaining their utility.

!!! info "Static Protocol"
    Defined by [PEP 544](https://peps.python.org/pep-0544/), it represents a protocol that `requires an explicit definition, typically through a typing.Protocol subclass` since Python 3.8. `Objects implementing a static protocol must provide every method declared in the protocol class, even if not all methods are needed by the program`.

__Key Differences between Dynamic and Static Protocols__:

1. An object can `implement only a part of a dynamic protocol and still be functional`, whereas a `static protocol mandates the provision of every method declared in the protocol class`, irrespective of the program's requirements.
1. `Static protocols can be verified by static type checkers`, which is not possible for dynamic protocols.

Python offers another explicit means of defining an interface in code: the `abstract base class (ABC)`.

## Programming Ducks - Dynamic Protocols

### Monkey Patching: Implementing a Protocol at Runtime

Monkey patching is dynamically `changing` a module, class, or function `at runtime`, to add features or fix bugs.  `It involves changing or adding attributes without altering its source code`.

??? warning
    While it can be a powerful tool in certain situations, `it should be used with caution as it can make code more difficult to understand and maintain`. Therefore, it is generally advisable to use monkey patching judiciously and consider alternative approaches, such as subclassing or proper design patterns, when possible.

??? example

    ``` py title="src/classes_objects/monkey_patching.py"
    --8<-- "src/classes_objects/monkey_patching.py"
    ```
    ```bash title="output"
    This is the original method.
    Patched behavior
    ```

## Goose Typing

In Python, the concept of `goose typing refers to a runtime type-checking approach that utilizes Abstract Base Classes (ABCs)`. Unlike languages with explicit interfaces, `Python relies on ABCs to define interfaces for the purpose of type checking`, both at runtime and with static type checkers.

`Abstract base classes enhance duck typing by introducing virtual subclasses, which are classes that do not directly inherit from a particular class but are still recognized by functions like isinstance() and issubclass()`. This runtime type checking approach is made possible by the usage of ABCs.

In practice, `goose typing allows the use of isinstance(obj, cls) where cls is an abstract base class with a metaclass of abc.ABCMeta`. It is important to note that sometimes there is no need to register a class explicitly for it to be recognized as a subclass of an ABC.

??? example "subclass of an ABC without register"

    ```pycon exec="1" source="console"
    >>> class Struggle:
    ...     def __len__(self): return 23
    >>> from collections import abc
    >>> print(isinstance(Struggle(), abc.Sized))
    ```

To summarize, goose typing involves:

1. `Creating subclasses from ABCs to explicitly indicate that you are implementing a previously defined interface`.
1. `Using ABCs for runtime type checking instead of concrete classes` as arguments for `isinstance` and `issubclass`.

By employing ABCs for type checking, you can achieve more flexibility in your code. This approach allows for `greater polymorphism`, as components can `implement required methods without necessarily explicitly subclassing the ABC`. If needed, a component can always be registered later to pass explicit type checks.

### Subclassing an ABC

When `subclassing` an Abstract Base Class (ABC), `the implementation of abstract methods is not checked during the import` of the module. Instead, it is c`hecked only at runtime when attempting to instantiate an object`. If `any of the abstract methods are not implemented`, a TypeError exception is raised with a message indicating that the abstract methods are missing, even if your class does not require these specific behaviors.

Therefore, `it's crucial to ensure that all required abstract methods are implemented in your subclass to avoid runtime errors`. Even if certain functionalities are not needed for a particular subclass, their implementation is still mandatory to satisfy the requirements of the ABC and ensure proper instantiation and functionality during runtime.

??? example

    ```python
    class MyABC(abc.ABC):
        @classmethod
        @abc.abstractmethod
        def an_abstract_classmethod(cls, ...):
            pass
    ```

### ABCs in the Standard Library

Abstract Base Classes (ABCs) are `primarily found in the collections.abc module`, although some others exist in modules like io and numbers. The `abc` module itself is also present, `containing the abc.ABC class`. While `every ABC depends on the abc module`, it is not necessary to import it explicitly unless you are creating a new ABC.

The `collections.abc` module is extensively used, and its [documentation features a helpful table](https://docs.python.org/3/library/collections.abc.html#collections-abstract-base-classes) that `summarizes the various ABCs, their relationships, as well as their abstract and concrete methods, often referred to as mixin methods`. This table provides a clear overview of the ABCs available in the standard library, allowing developers to understand their functionalities and relationships at a glance.

### A Virtual Subclass of an ABC

In goose typing, one of the notable features is the ability to `register a class as a virtual subclass of an Abstract Base Class (ABC), even if the class does not inherit from it`. By registering the class as a virtual subclass, you are essentially `asserting that the class faithfully implements the interface defined in the ABC, and Python will accept this assertion without performing a direct check`. However, if the class fails to implement the necessary methods as promised, Python will raise the usual runtime exceptions.

This registration process involves `calling a class method`, often named `register`, on the `ABC`. `Once the class is registered, it becomes a virtual subclass of the ABC`, and Python recognizes it as such through functions like `issubclass`. It's important to note that the `registered class does not inherit any methods or attributes from the ABC`. The register method can be invoked as a standard function, or it can be used as a decorator to streamline the process.

It's important to understand that [inheritance is guided by a special class attribute named __mro__](inheritance.md#multiple-inheritance---execution-order-and-mro-attritube).  Notably, `ABCs are not included in the __mro__ attribute`, meaning `they do not participate in the regular inheritance hierarchy`.
