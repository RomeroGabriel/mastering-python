# Exception Handling

To ensure consistency and proper handling, all exceptions must be instances of a class that **derives from the BaseException class**. This principle helps maintain code clarity and enables developers to catch and respond to specific error scenarios effectively.

## Handiling Exceptions

### Selected Exception

```pycon exec="1" source="console" title="selecet_exc.py"
>>> try:
...     x = "hello"
...     y = sum(x)
... except TypeError:
...     print("Operation invalid")
```

### Multiple Handlers Expcetions

```pycon exec="1" source="console" title="multi_selecet_exc.py"
>>> try:
...     x = "hello"
...     z = x / 2
...     y = sum(x)
... except (ValueError, TypeError, NameError):
...     print("Operation invalid")
...     print()
```

```pycon exec="1" source="console" title="multi_selecet_exc2.py"
>>> import sys
>>> try:
...    f = open('myfile.txt')
...    s = f.readline()
...    i = int(s.strip())
... except OSError as err:
...    print("OS error: {0}".format(err))
... except ValueError:
...    print("Could not convert data to an integer.")
... except BaseException as err:
...    print(f"Unexpected {err=}, {type(err)=}")
...    raise
```

### BaseExceptions as a Wildcard

By virtue of all exceptions inheriting from BaseException, it is possible to utilize the "except" statement to **capture any exception**.

```pycon exec="1" source="console" title="base_exc.py"
>>> import sys
>>> try:
...    f = open('myfile.txt')
...    s = f.readline()
...    i = int(s.strip())
... except BaseException as err:
...    print(f"Unexpected {err=}, {type(err)=}")
```

### Exception Properties Analyses

```pycon exec="1" source="console" title="base_exc.py"
>>> try:
...    raise Exception('spam', 'eggs')
... except Exception as inst:
...    print(type(inst))
...    print(inst.args)
...    x, y = inst.args
...    print('x =', x)
...    print('y =', y)
```

## Raise Exceptions

```python
raise ValueError  # shorthand for 'raise ValueError()'
```

```python
try:
    raise NameError('Hi There')
except NameError:
    print('An exception flew by!')
    raise
```

### Exceptions Chaining

The **raise** statement in Python enables the option of chaining exceptions, facilitating error handling and flow control within the code.

```python title="exc_chaning.py"
>>> def func():
...    raise ConnectionError
>>> try:
...    func()
... except ConnectionError as exc:
...    raise RuntimeError('Failed to open database') from exc
```

```pycon exec="1" source="console" title="exc_chaning_result.py"
>>> def func():
...    raise ConnectionError

>>> try:
...    func()
... except ConnectionError as exc:
...    raise RuntimeError('Failed to open database') from exc

Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 2, in func
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: Failed to open database
```

## User-definied Exceptions

When creating **user-defined exceptions**, it is essential to ensure they are derived either **directly or indirectly from the built-in Exception class**. Conventionally, these custom exceptions are named with endings such as "Error," following a clear and descriptive naming pattern for enhanced code readability.

```python title="db_exception.py"
from dataclasses import dataclass, field

@dataclass
class DatabaseConnectionError(Exception):
    message: str = field(init=False, default="Couldn't connect to database")
```

## References

- [Python Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Python Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
- [Real Python Exceptions](https://realpython.com/python-exceptions/)
