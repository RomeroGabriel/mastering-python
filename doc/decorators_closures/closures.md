# Closures

To comprehend closures, it's essential to have a solid understanding of [variable scopes](../functions/variables_scope.md).

It's not the same thing that anonymous functions. `Closure focus on nested functions`, that one function can access nonglobal variable that are defined outside of its body, does not matter whether the function is anonymous or not.

???+ example

    ```pycon exec="1" source="console"
    >>> def make_averager():
    ...     series = []
    ...     test_nice = "nice"
    ...     def averager(new_value):
    ...         series.append(new_value) # accessing series
    ...         return sum(series) / len(series)
    ...     return averager
    >>> avg = make_averager()
    >>> print(avg(10))
    >>> print(avg(11))
    >>> print(avg(15))
    >>> print(avg.__code__.co_varnames)
    >>> print(f"freevars: {avg.__code__.co_freevars}")
    >>> print(f"__closure__: {avg.__closure__}")
    >>> print(avg.__closure__[0].cell_contents)
    ```

    In this is example, `make_averager function return a callable object`. The `averager` function updates the series list and return the current mean.

## How it Works

> Read [nonlocal scope](../functions/variables_scope.md#types-of-scope) to understand free variables.

Using the example as base, the `averager function is a closure`. The `averager` function `can access the series variable` defined on make_averager because `series is a free variable`. This is a technical term meaning a variable that is not bound in the local scope. Only variables referenced on the closure are mappend, like is possible to see in the test_nice variable.

Closures functions is only available inside the outer function, so its commom to return the closure function to be consume externally.

## Assigning Variables and nonlocal Keyword used

In the example, it `worked because series is a list`, which can be changed using 'series.append()'. But `if series were an integer`, which can't be altered, and the code tried something like `series += new_value`, `it would cause an error`: "local variable 'series' referenced before assignment". This occurs because `when you attempt to rebind series` (as in 'series += new_value'), it `implicitly creates a local variable called series`, and at this point, series is no longer a free variable.

To resolve this issue, you need to use the `nonlocal` keyword, which allows you to declare a free variable. When a `new value is assigned to a nonlocal variable`, the binding stored in the closure is updated.

```pycon exec="1" source="console" title="example_with_nonlocal.py"
>>> def make_averager():
...    count = 0
...    total = 0
>>>    def averager(new_value):
...        nonlocal count, total
...        count += 1
...        total += new_value
...        return total / count
...    return averager
>>> avg = make_averager()
>>> print(avg(10))
>>> print(avg(11))
>>> print(avg(15))
```

## References

- [Fluent Python, 2nd Edition](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/)
