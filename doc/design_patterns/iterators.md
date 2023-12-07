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

!!! example "Check issubclass and isinstance"

    ``` py title="src/design_patterns/iterators/isisntancecheck.py"
    --8<-- "src/design_patterns/iterators/isisntancecheck.py"
    ```

    ```bash title="output"
    Class Test is an Iterable subclass? True
    test_var instance Test is an Iterable instance? True
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

## Avoid Making the Iterable an Iterator for Itself

`A common mistake when creating iterables and iterators is mixing up the two`. `Iterables have an __iter__ method that crafts a new iterator` every time it's called. `Iterators`, on the flip side, implement a `__next__` method to provide individual items and an `__iter__` method that returns self.

!!! tip
    In essence, iterators are naturally iterable, but `iterables are not iterators`.

While it might seem like a good idea to give the both `__next__` and `__iter__` methods to a class, turning each instance into an iterable and an iterator at the same time, it's generally not a wise move.

Following the Iterator pattern, `it's important that we can get multiple independent iterators from the same iterable`. Each iterator should maintain its own internal state, meaning a proper implementation should create a new, independent iterator every time iter(my_iterable) is called.

## Generators

`A Python function becomes a generator function simply by having the yield keyword in its body`. When this function is called, it returns a generator object, essentially making it a generator factory. `The primary distinction between a regular function and a generator function lies in the presence of the yield keyword`.

A generator function constructs a `generator object that encapsulates the function's body`. Upon invoking `next()` on the generator object, `execution progresses to the next yield in the function body`. The `next()` call yields the value when the function body is paused. Eventually, when the function body completes, the enclosing generator object, as per the Iterator protocol, raises `StopIteration`.

!!! example

    ``` py title="src/design_patterns/iterators/generator_example.py"
    --8<-- "src/design_patterns/iterators/generator_example.py"
    ```

    ```bash title="output"
    Start test gen
    ---> 1
    After yield 1
    ---> 2
    Finish test gen
    ```

!!! example "Using with Iterator"

    ``` py title="src/design_patterns/iterators/using_generators.py"
    --8<-- "src/design_patterns/iterators/using_generators.py"
    ```

    ```bash title="output"
    Corinthians
    Lakers
    Liverpool
    ```
