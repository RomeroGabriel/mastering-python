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

## Programming Ducks

## Goose Typing
