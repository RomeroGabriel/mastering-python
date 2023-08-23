# Decorators

A decorator is a `function that takes another function (the decorated function) as its input`. It can perform some actions with the decorated function and either return it or substitute it with another function or callable object. To become proficient in using decorators, it's important to grasp the concept of [closures](closures.md).

In essence, `decorators are syntactic sugar`, as you can always directly call a decorator just like any regular callable as demonstrated in `decorator_example.py`. In summary, decorators are:

1. A decorator is a function or another callable;
1. A decorator can replace the decorated function with a different one or perform pre- or post-processing;
1. `Decorators are executed immediately when a module is loaded`;

??? example "Decorator Example"

    ```pycon exec="1" source="console"  title="decorator_example.py"
    >>> def decorate(func):
    ...     def inner():
    ...         print('running inner()')
    ...         func()
    ...     return inner
    ...
    >>> @decorate
    >>> def target():
    ...    print('running target()')
    >>> target()
    ...
    >>> print("EQUALS TO:")
    >>> def target():
    ...    print('running target()')
    >>> target = decorate(target)
    >>> target()
    ```

## Decorators Execution Flow

`Decorators are executed as soon as the module is imported`, but the `decorated functions only run when they are explicitly called`. This emphasizes the `distinction between "import time" and "runtime"`.

??? example "Decorator Execution Flow"

    ``` py title="src/decorators/decorator_execution.py"
    --8<-- "src/decorators/decorator_execution.py"
    ```

    ``` title="output"
    Executing decorator!! COUNT: [<function f1 at 0x7f8c665e8d60>]
    Executing decorator!! COUNT: [<function f1 at 0x7f8c665e8d60>, <function f2 at 0x7f8c665e8680>]
    Starting MAIN!
    decorator_log on MAIN -> [<function f1 at 0x7f8c665e8d60>, <function f2 at 0x7f8c665e8680>]
    F1 execution!!
    F2 execution!!
    F3 execution!!
    ```
