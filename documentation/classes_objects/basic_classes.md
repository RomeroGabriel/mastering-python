# Classes

## Classmethod x Staticmethod

The `@classmethod` decorator: Method operating on the class, not instances. `Receives the class as its first argument, often used for alternative constructors`.

The `@staticmethod` decorator: `Method with no special first argument`. Functions like a regular function defined in a class, not dependent on class or instance. Typically used for class-related utility functions.

```pycon exec="1" source="console" title="class_static_example.py"
>>> class Test:
...     @classmethod
...     def class_test(*args):
...         print(args)
...     @staticmethod
...     def static_test(*args):
...         print(args)
>>> Test.class_test()
>>> Test.static_test()
>>> Test.class_test(123)
>>> Test.static_test(123)
```

## References

- [Fluent Python, 2nd Edition](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/)
