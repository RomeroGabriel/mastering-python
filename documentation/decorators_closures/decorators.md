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

## Stacked Decorators

When a function is decorated with more than one decorator, the `innermost decorator is applied first`. Then, the function it returns is passed forward to the next decorator in the stack.

??? example "Stacked Decorators"

    ```python title="stacked_decorators.py"
    >>> @decorator1
    >>> @decorator2
    >>> def fun(n):
    ...     ...
    >>> print("Is the same as this: ")
    >>> fun = decorator2(decorator1(my_fn))
    ```

## Parameterized Decorators

When using decorators in Python, the `decorated function is passed as the first argument to the decorator function`. If you want a decorator to accept additional arguments, you need to create a `decorator factory`. `This factory function takes those extra arguments` and returns a decorator, which can then be applied to the function you want to decorate.

??? example "Simple Parameterized Decorator"

    ```pycon exec="1" source="console"  title="parameter_decorator_example.py"
    >>> def nice_logger(extra_info=True):
    ...     def decorate(func):
    ...         print("passing nice_logger")
    ...         if extra_info:
    ...             print(f"printing extra_info: {extra_info}. func {func}")
    ...         return func
    ...     return decorate

    >>> @nice_logger(extra_info=False)
    >>> def f1():
    ...     print("f1()")
    
    >>> @nice_logger()
    >>> def f2():
    ...     print("f2()")

    >>> @nice_logger()
    >>> def f3():
    ...     print("f3()")
    >>> f1()
    >>> f2()
    >>> f3()
    ```

    1. nice_logger is not a decorator but a `decorator factory`;
    1. `decorate inner function is the actual decorator`, taking a function as an argument;
    1. Even when no parameters are passed, nice_logger must still be called as a function nice_logger();
    1. The main point is that `nice_logger() returns decorate, which is then applied to the decorated function`.
    1. using @ syntax, is equivalent to `nice_logger()(f1) or nice_logger(extra_info=False)(f1)`

??? example "Parameterized Decorator passing arguments"
    ```pycon exec="1" source="console"  title="parameter_decorator_example.py"
    >>> def nice_logger(extra_info=""):
    ...     def decorate(func):
    ...         def logger(*_args):
    ...             result = func(*_args)
    ...             if extra_info:
    ...                 print(f"{extra_info}: {result}")
    ...             return result
    ...         return logger
    ...     return decorate

    >>> @nice_logger(extra_info="F1: The final result is ")
    >>> def f1(num1):
    ...     return 10 + num1
    
    >>> @nice_logger()
    >>> def f2(num1):
    ...     return 20 + num1

    >>> @nice_logger()
    >>> def f3(num1):
    ...     return 30 + num1
    >>> f1(10)
    >>> f2(10)
    >>> f3(10)
    ```

    1. The key distinction here is that the decorated function accepts parameters.
    1. The `logger function` returns the result of the decorated function.
    1. The decorate function returns the logger function.

## Class-Based Decorator

Instead of using a function to decorate a function, `you can use a class object that implements the __call__ method`. This allows you to create decorators using classes, providing more flexibility and control over the decoration process.

??? example "Parameterized Decorator passing arguments"

    ``` py title="src/decorators/class_decorator.py"
    --8<-- "src/decorators/class_decorator.py"
    ```

## References

- [Fluent Python, 2nd Edition](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/)
- [PythonDecoratorLibrary](https://wiki.python.org/moin/PythonDecoratorLibrary#Asynchronous_Call)
