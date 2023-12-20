# Itertools Module

The `itertools` module in Python is a powerful utility module that provides a collection of functions for working with `iterators and iterables` more efficiently. These functions offer convenient tools for tasks such as creating iterators, combining and chaining iterables, and performing advanced operations on sequences.

## itertools.compress(it, selector_it)

`Consumes two iterables in parallel`. yields items from it whenever the corresponding item in `selector_it` is truthy.

!!! example

    ``` py title="src/builtint_modules/itertools/compress.py"
    --8<-- "src/builtint_modules/itertools/compress.py"
    ```

    ```bash title="output"
    ['A', 'C', 'D', 'F']
    ```

## itertools.dropwhile(predicate, it)

Consumes it, `skipping items while predicate computes truthy`, then yields every remaining item (no further checks).

!!! example

    ``` py title="src/builtint_modules/itertools/dropwhile.py"
    --8<-- "src/builtint_modules/itertools/dropwhile.py"
    ```

    ```bash title="output"
    ['G', 'J', 'I', 'O', 'U']
    ```

## itertools.filterfalse(predicate, it)

Same as filter, with the `predicate logic negated`: yields items whenever predicate computes falsy.

!!! example

    ``` py title="src/builtint_modules/itertools/filterfalse.py"
    --8<-- "src/builtint_modules/itertools/filterfalse.py"
    ```

    ```bash title="output"
    ['G', 'J']
    ```

## itertools.islice(it, stop) or islice(it, start, stop, step=1)

Yields items from a slice of it, `similar to s[:stop] or s[start:stop:step] except it can be any iterable`, and the operation is lazy.

!!! example

    ``` py title="src/builtint_modules/itertools/islice.py"
    --8<-- "src/builtint_modules/itertools/islice.py"
    ```

    ```bash title="output"
    [0, 1, 2, 3]
    [4, 5, 6]
    [1, 3, 5]
    ```

## itertools.takewhile(predicate, it)

`Yields items while predicate computes truthy`, then stops and no further checks are made.

!!! example

    ``` py title="src/builtint_modules/itertools/takewhile.py"
    --8<-- "src/builtint_modules/itertools/takewhile.py"
    ```

    ```bash title="output"
    [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
    [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    ```

## itertools.accumulate(it, [func])

`Yields accumulated sums`, if func is provided, yields the result of applying it to the first pair of items, then to the first result and next item, etc.

!!! example

    ``` py title="src/builtint_modules/itertools/accumulate.py"
    --8<-- "src/builtint_modules/itertools/accumulate.py"
    ```

    ```bash title="output"
    [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
    ```

## itertools.starmap(func, it)

`Applies func to each item of it`, yielding the result; the input iterable should yield iterable items iit, and func is applied as func(*iit).

!!! example

    ``` py title="src/builtint_modules/itertools/starmap.py"
    --8<-- "src/builtint_modules/itertools/starmap.py"
    ```

    ```bash title="output"
    [6, 20, 12]
    ```

## itertools.chain(it1, …, itN)

Yields all items from it1, then from it2, etc., seamlessly.

!!! example

    ``` py title="src/builtint_modules/itertools/chain.py"
    --8<-- "src/builtint_modules/itertools/chain.py"
    ```

    ```bash title="output"
    ['d', 'f', 'k', 'l', 'n', 'p', 'a', 'e', 'i', 'o', 'u']
    ```

## itertools.chain.from_iterable(it)

Yields all items from each iterable produced by `it`, one after the other, seamlessly. `it will be an iterable where the items are also iterables, for example, a list of tuples`.

!!! example

    ``` py title="src/builtint_modules/itertools/chain_from_iterable.py"
    --8<-- "src/builtint_modules/itertools/chain_from_iterable.py"
    ```

    ```bash title="output"
    [0, 'a', 1, 'e', 2, 'i', 3, 'o', 4, 'u']
    ```

## itertools.product(it1, …, itN, repeat=1)

`Cartesian product`: yields N-tuples made by combining items from each input iterable, like nested for loops could produce. `repeat allows the input iterables to be consumed more than once`.

!!! example

    ``` py title="src/builtint_modules/itertools/product.py"
    --8<-- "src/builtint_modules/itertools/product.py"
    ```

    ```bash title="output"
    [('A', 0), ('A', 1), ('B', 0), ('B', 1), ('C', 0), ('C', 1)]
    [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
    ```

## itertools.zip_longest(it1, …, itN, fillvalue=None)

`Yields N-tuples built from items taken from the iterables in parallel`, stopping only when the last iterable is exhausted, `filling the blanks with the fillvalue`.

!!! example

    ``` py title="src/builtint_modules/itertools/zip_longest.py"
    --8<-- "src/builtint_modules/itertools/zip_longest.py"
    ```

    ```bash title="output"
    [('A', 0), ('B', 1), ('C', 2), (None, 3), (None, 4)]
    [('A', 0), ('B', 1), ('C', 2), ('!!!', 3), ('!!!', 4)]
    ```
