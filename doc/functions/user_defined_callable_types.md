# User-Defined Callable Types

In Python, we can make arbitrary objects behave like functions by implementing a `__call__` instance method. This simple approach allows us to create function-like objects with internal state that persists across invocations. By defining the `__call__` method, we enable instances of the class to be callable, just like regular functions.

```pycon exec="1" source="console" title="user_callable_object.py"
>>> import random
>>> class BingoCage:
>>>     def __init__(self, items):
...        self._items = list(items)  
...        random.shuffle(self._items)  
>>>     def pick(self):
...        try:
...            return self._items.pop()
...        except IndexError:
...            raise LookupError('pick from empty BingoCage')  
>>>     def __call__(self):
...        return self.pick()
>>> bingo = BingoCage(range(3))
>>> print(bingo.pick())
>>> print(bingo())
>>> print(callable(bingo))
```

## References

- [Fluent Python, 2nd Edition](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/)
