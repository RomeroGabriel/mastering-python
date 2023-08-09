# List

A list is a built-in data structure in Python and is classified as a type of [sequence data structure](sequence.md).

## Characteristics

1. [Mutable Sequence](sequence.md#mutable-x-immutable)
1. [Container Sequence](sequence.md#container-x-flat)

## List Comprehensions

List comprehensions provide a concise method for `creating lists`. [Generator expressions for other kinds of sequences](sequence.md#generator-expressions). They are commonly used to generate new lists by `applying operations to elements of an existing sequence or iterable`, or to create a sublist of elements that fulfill specific conditions.Using list comprehensions can significantly `enhance the readability of your code`.

A list comprehension consists of `brackets` containing an expression followed by a `for clause, then zero or more for or if clauses`. The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.

### Examples

```pycon exec="1" source="console" title="listcomp.py"
>>> print("comparison with map function")
>>> squares = list(map(lambda x: x**2, range(10)))
>>> print(f"squares => {squares}")
>>> squares = [x**2 for x in range(10)]
>>> print(f"squares => {squares}")

>>> print("comparison with filter function")
>>> symbols = '$¢£¥€¤'
>>> beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
>>> print(f"beyond_ascii => {beyond_ascii}")
>>> beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
>>> print(f"beyond_ascii => {beyond_ascii}")

>>> print("Multiple listcomp")
>>> combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
>>> print(combs)
>>> combs = []
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...         if x != y:
...             combs.append((x, y))
>>> print(combs)
```

## list.sort x sorted Build-In

1. The list.sort method sorts a list in place (`without making a copy`):
    1. It returns None - This follows an `important Python API convention: functions or methods that change an object in place should return None to make it clear to the caller`.
    1. We cannot chain calls to these methods.
1. The sorted function `creates a new list and returns it`:
    1. It accepts any iterable object as an argument.
    1. It always returns a newly created list.
1. Both methods take two optional keyword-only arguments:
    1. `reverse`: If True, the items are returned in descending order. The default is False.
    1. `key`: A one-argument function to be applied to each item.

```pycon exec="1" source="console" title="gen_enx.py"
>>> fruits = ['grape', 'raspberry', 'apple', 'banana']
>>> print(f"sorted: {sorted(fruits)}, fruits: {fruits}")
>>> print(f"sorted: {sorted(fruits, reverse=True)}, fruits: {fruits}")
>>> print(f"sorted: {sorted(fruits, key=len)}, fruits: {fruits}")
>>> print(f"sorted: {sorted(fruits, key=len, reverse=True)}, fruits: {fruits}")
>>> fruits.sort()
>>> print(f"Now fruits changed: {fruits}")
```

## When a List is not the answer

1. An `array` saves a lot of memory when you need to handle millions of floating-point;
1. A `deque` (double-ended queue) is more efficient `FIFO` (First-In First-out) data structure;
1. `Sets` are optimized for `fast membership checking`.

## Extras

1. [Methods for lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
1. [Using Lists as Stacks](https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks)
1. [Using Lists as Queues](https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-queues)

## References

- [Fluent Python, 2nd Edition](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/)
- [Python - More on List](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
