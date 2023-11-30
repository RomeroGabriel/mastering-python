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

```pycon exec="1" source="console" title="range.py"
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

## try

```pycon exec="1" source="console" title="try.py"
>>> try:
...    zero_division = 10 / 0
... except ZeroDivisionError as zero_error:
...     print(f"ERROR: {zero_error}")
... except:
...     print("Global except clause")
... finally:
...     print("Justing print the finally")
```

## break, continue and else on loops

- The **break** statement breaks out the innermost enclosing for or while loop.
- The **else** statement in loops is **executed when the loop terminates through exhaustion**, but not when the loop is terminated by a break statement.

```pycon exec="1" source="console" title="break_else.py"
>>> for n in range(2, 10):
>>>    for x in range(2, n):
...        if n % x == 0:
...            print(n, 'equals', x, '*', n//x)
...            break
...    else:
...        # loop fell through without finding a factor
...        print(n, 'is a prime number')
```

- The **continue** statement continues with the next iteration of the loop.

```pycon exec="1" source="console" title="continue.py"
>>> for num in range(2, 10):
>>>    if num % 2 == 0:
...        print("Found an even number", num)
...        continue
...    print("Found an odd number", num)
```

## match

- A **match** statement takes an exmpression and compares its value to sucessive patterns using the case blocks.
- This is similar to a switch statement but it's more similiar to patter matching.
- **Only the first pattern** that matches gets executed.
- There are many use cases that will be explorer more in this documentation.

```pycon exec="1" source="console" title="match.py"
>>> def http_error(status):
>>>    match status:
...        case 400:
...            return "Bad request"
...        case 404:
...            return "Not found"
...        case 418:
...            return "I'm a teapot"
...        case _:
...            return "Something's wrong with the internet"
```

## References

- [Python - 8. Compound statements](https://docs.python.org/3/reference/compound_stmts.html#compound-statements)
- [Python - 4. More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html#)
