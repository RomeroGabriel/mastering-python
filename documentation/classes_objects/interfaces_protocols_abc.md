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
    ![Typing Map. Image from Fluent Python, 2nd Edition](https://raw.githubusercontent.com/RomeroGabriel/mastering-python/main/documentation/images/classes_objects/typing_map.png)
    [Typing Map. Image from Fluent Python, 2nd Edition](https://raw.githubusercontent.com/RomeroGabriel/mastering-python/main/documentation/images/classes_objects/typing_map.png)

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
