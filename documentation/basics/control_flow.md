# Control Flow

Listing the fundamental and commonly used control flow structures in Python.

## if

```pycon exec="1" source="console" title="if.py"
>>> x = 42
>>> if x < 0:
...     x = 0
...     print('Negative changed to zero')
... elif x == 0:
...     print('Zero')
... elif x == 1:
...     print('Single')
... else:
...     print('More')
```

### Short hand if

```pycon exec="1" source="console" title="short_if.py"
>>> a = 25
>>> b = 15
>>> if a > b: print("A is greater than B")

>>> print("B") if a <= b else print("A")
```

## while

```pycon exec="1" source="console" title="while.py"
>>> n = 5
>>> while n > 1:
...     print(n)
...     n = n - 1
```

## for

```pycon exec="1" source="console" title="for.py"
>>> words = ['cat', 'window', 'defenestrate']
>>> for w in words:
...    print(w, len(w))
```

## range

```pycon exec="1" source="console" title="for.py"
>>> for i in range(3):
...    print(i)
... print("range(3)--------->")

>>> for i in range(5, 10):
...    print(i)
... print("range(5, 10)--------->")

>>> for i in range(0, 10, 2):
...    print(i)
... print("range(0, 10, 2)--------->")

>>> a = ['Mary', 'had', 'a', 'little', 'lamb']
>>> for i in range(len(a)):
...    print(i, a[i])
... print("range(len(a))--------->")
```

## with

test

## try

test

## match

test

## break, continue and else on loops

test

## References

- [Python - 8. Compound statements](https://docs.python.org/3/reference/compound_stmts.html#compound-statements)
- [Python - 4. More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html#)
