# Parameters

In Python, parameter passing follows the concept of `call by sharing`. This means that **each formal parameter of the function receives a copy of each reference in the arguments.** As a result, the *parameters inside the function become aliases of the actual arguments*. While the `function can modify any mutable object passed as a parameter`, it cannot change the identity of those objects.

Understanding this mechanism is crucial for working with functions in Python, as it ensures that modifications to parameters within a function do not affect the original objects in the calling code.

```pycon exec="1" source="console" title="parameters.py"
>>> def nice_function(a, b):
...     a += b
...     return a
>>> x = 1
>>> y = 2
>>> print(f"nice_function(x, y): {nice_function(x, y)}")
>>> print(f"X and Y didn't change: {x , y}")
>>> print("Reason: int is immutable")
>>> a = [1, 2]
>>> b = [3, 4]
>>> print(f"nice_function(a, b): {nice_function(a, b)}")
>>> print(f"A and B change: {a , b}")
>>> print("Reason: list is mutable")
```

## Default Arguments

```pycon exec="1" source="console" title="default_arguments.py"
>>> def nice_some(a = 2, b =2):
...     # int is immutable, SO ALL GOOD!
...     return a + b
>>> print(nice_some())
>>> print(nice_some(50))
>>> print(nice_some(50, 50))
```

### Mutable Types as Deafults: Bad Idea

Default values in Python functions are **evaluated at the time of function definition**, in the defining scope. As a result, the `default value is evaluated only once`, and this becomes significant when the default value is a mutable object, like a list, dictionary, or instances of most classes.

If a default value is a mutable object, and you `modify it within the function, the change will affect all future calls to the function`. This is because instances that don't receive an initial value for a mutable default parameter end up sharing the same variable reference.

To avoid unexpected behavior, it's **common to use None as the default value for parameters that may receive mutable values**. By doing so, you ensure that each call to the function receives its independent mutable object, preventing any unintended side effects across different function calls.

```pycon exec="1" source="console" title="default_mutable_arguments.py"
>>> def f(a, L=[]):
...    L.append(a)
...    return L

>>> print(f(1))
>>> print(f(2))
>>> print(f(3))
```

``` py title="src/functions/deep_mutable_arg.py"
--8<-- "src/functions/deep_mutable_arg.py"
```

## Positional or Keyword Parameters

If the parameter type (positional or keyword) is not explicitly specified, it is possible to pass the argument in both ways.

```pycon exec="1" source="console" title="positional_keyword.py"
>>> def example_function(a, b, c):
...    print(a, b, c)
>>> # Both ways of calling the function are valid:
>>> example_function(1, 2, 3)       # Positional arguments
>>> example_function(c=3, b=2, a=1) # Keyword arguments
```

## Positional-Only Parameters

Positional-only parameters in Python functions are ordered in a way that their `sequence matters`, and they cannot be passed using keywords. These parameters are designated by being `placed before a forward-slash (/) in the function definition`. The forward-slash serves as a logical separator, indicating the boundary between the positional-only parameters and the rest of the parameters.

```pycon exec="1" source="console" title="positional_only.py"
>>> def example_function(a, b, /, c, d):
...     print(a, b, c, d)
... # Calling the function using positional arguments only:
>>> example_function(1, 2, 3, 4)
... # Using positional and keyword arguments together:
>>> example_function(3, 1, c=2, d=7)
... # example_function(3, b=1, c=2, d=7) b=1 generates an error because B cannot be keyword
```

## Keyword-Only Parameters

To mark parameters as keyword-only, indicating the parameters must be passed by keyword argument, place an `* in the arguments list just before the first keyword-only parameter`.

```pycon exec="1" source="console" title="keyword_only.py"
>>> def example_function(a, b, *, c, d):
...     print(a, b, c, d)
... # Calling the function using positional arguments only:
>>> example_function(1, 2, c=3, d=4)
... # Using positional and keyword arguments together:
>>> example_function(3, b=1, c=2, d=7) # No problem, just C and D NEEDS to be keyword
... # example_function(3, 1, 2, d=7) ERROR C is not Keyword
```

## Positional and Keyword Parameters

If `/` and `*` are not present in the function definition, arguments may be passed to a function by position or by keyword.

```text
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
```

## Arbitrary Argument Lists

Python functions can be defined to `accept an arbitrary number of arguments by using the asterisk (*) symbol before the parameter name`. This allows the function to be called with any number of arguments, and these arguments will be `bundled together into a tuple.`

```pycon exec="1" source="console" title="arbitrary_args.py"

>>> def write_multiple_items(file, separator, *args):
...    file.write(separator.join(args))

```

Normally, these arbitrary argumen are typically placed last in the list of formal parameters of a function. This allows them to collect any additional input arguments that are passed to the function. `After the *args parameter, any subsequent formal parameters are considered 'keyword-only' arguments`, which means they can only be used as keywords when calling the function, rather than being passed as positional arguments.

```pycon exec="1" source="console" title="arbitrary_args2.py"

>>> def example_function(a, b, *args, c, d):
...    print(f"a: {a}, b: {b}")
...    print(f"Additional arguments {args}, type {type(args)}")
...    print(f"c: {c}, d: {d}")
>>> example_function(1, 2, 3, 4, 5, c=6, d=7)
>>> example_function(10, 20, c=30, d=40)
```

## Unpacking Argument Lists

```pycon exec="1" source="console" title="unpacking_args.py"

>>> def parrot(voltage, state='a stiff', action='voom'):
...    print("-- This parrot wouldn't", action, end=' ')
...    print("if you put", voltage, "volts through it.", end=' ')
...    print("E's", state, "!")
>>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
>>> parrot(**d)
```

## References

- [Python - 4.8. More on Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions)

- [Fluent Python, 2nd Edition](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/)
