# Dictionaries

A dict is a built-in data structure in Python.

## Characteristics

1. [Mutable Sequence](sequence.md#mutable-x-immutable)
1. Implemented using a hash table, highly optimized
1. ??? info "`Key` must be hashable objects"
    They must implement proper `__hash__` and `__eq__` methods;

1. ??? info "`Item access by key is very fast`"
    Python can locate a key directly by computing the hash code of the key;

1. `Key ordering is preserved` as a side effect of a more compact memory layout;
1. ??? info "Dicts inevitably have a significant memory overhead"
    They most compact internal data structure for a container would be an array of pointers to the items. Compared to that, a hash table `needs to store more data per entry, and Python needs to keep at least one-third of the hash table rows empty to remain efficient`

## Dict Comprehensions

A dictcomp (dict comprehension) build a dict instance by taking key:value pairs from any iterable.

```pycon exec="1" source="console" title="dict_compre.py"
>>> dial_codes = [
...     (880, 'Bangladesh'),
...     (55,  'Brazil'),
...     (86,  'China'),
...     (91,  'India'),
... ]
>>> dict_country = { country: code 
...    for code, country in dial_codes }
>>> print(dict_country)
```

## Unpacking Mappings

Similar to [sequence unpacking](sequence.md#unpacking), you can `extract elements from a dictionary by using the * operator`. When you use a `single *, only the key` is returned, but when you `use **, both the key and the value` are returned.

```pycon exec="1" source="console" title="dict_unpack.py"
>>> def dump(*args,**kwargs):
...     print(f"args: {args} => just X, since we just unpack the key")
...     print(f"kwargs: {kwargs}")
>>> dump(*{'x': 1}, y=2, **{'z': 3})
```

## Merging Mappings

> Python 3.9 and above.

You can `merge mappings using | and |=`, which are also used as set union operators. The `| operator creates a new dictionary`, while the `|= operator updates an existing mapping in place`.

```pycon exec="1" source="console" title="merge_maps.py"
>>> d1 = {'a': 1, 'b': 3}
>>> d2 = {'a': 2, 'b': 4, 'c': 6}
>>> merged_dicts = d1 | d2
>>> print(f"merged_dicts => {merged_dicts} ============ d1 = {d1} and d2 {d2}")
>>> print("ATTENTION: Please note that, in cases where keys have the same values, the values from d2 (on the right side of the operation) have been retained.")
>>> print("--------------------------")
>>> d1 |= d2
>>> print(f"d1 = {d1} and d2 {d2}. Now d1 was updated")
```

## Pattern Matching

> Available in Python 3.10 and above!

In Python's pattern matching, the `subject` is the data following the `match` keyword, which Python aims to `match with patterns in each case clause`.  One key improvement of match over switch is `destructuring` - a more advanced form of unpacking the subject. A case clause has two parts: a `pattern` and an `optional guard with the if keyword`.

For subject `mapping pattern` matching, the following is necessary:

1. The subject  is a instance of any actual or virtual subclass of `collections.abc.Mapping`;
1. The `key orders is irrelevant`, even for OrderedDict;
1. Mapping patterns succeed on `partial match`.
1. You can prefix one variable with `** to capture extra key-value pairs` - It must be the last in the pattern;

```pycon exec="1" source="console" title="pattern_matching.py"
>>> def get_creators(record: dict) -> list:
...     match record:
...         case {'type': 'book', 'api': 2, 'authors': [*names]}:
...             print("type == book, api == 2 and ''authors' key mapped to sequence'")
...             return names
...
...         case {'type': 'book', 'api': 1, 'author': name}:
...             print("type == book, api == 2 and 'authors' key mapped to any object")
...             return [name]
...
...         case {'type': 'book'}:
...             print("No creators on dict")
...             raise ValueError(f"Invalid 'book' record: {record!r}")
...
...         case _:
...             raise ValueError(f'Invalid record: {record!r}')
... 
>>> b1 = dict(api=1, author='Douglas Hofstadter',
...         type='book', title='Gödel, Escher, Bach')
>>> print(f"get_creators of b1: {get_creators(b1)}")
>>> print()
>>> from collections import OrderedDict
>>> b2 = OrderedDict(api=2, type='book',
...         title='Python in a Nutshell',
...         authors='Martelli Ravenscroft Holden'.split())
>>> print(f"get_creators of b2: {get_creators(b2)}")
>>> print()
>>> try:
...     get_creators({'type': 'book', 'pages': 770})
... except BaseException as err:
...     print(f"Error: {err}")
>>> print()
>>> try:
...     get_creators('Spam, spam, spam')
... except BaseException as err:
...     print(f"Error: {err}")
```

```pycon exec="1" source="console" title="pattern_matching_partial_match.py"
>>> food = dict(category='ice cream', flavor='vanilla', cost=199)
>>> match food:
...     case {'category': 'ice cream', **details}:
...         print(f'Ice cream details: {details}')
```

## Getting, Inserting or Updating

## Getting

Dict acess with d[k] raises an error when k is not existing key. d.get(k, default) is an alternative whenever a default value is more convenient that handling KeyError

## Handling Missing Keys

## Variations of Dict

## Immutable Mappings

## References

- [Fluent Python, 2nd Edition](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/)
