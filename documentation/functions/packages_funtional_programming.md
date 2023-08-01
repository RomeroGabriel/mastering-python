# Packages for Funtional Programming

## Operator and Functools Modules

The `operator` module provides functions equivalents for dozens of operators so you don’t have to code trivial function like `lambda a, b: a*b.`

The `functools` module provides several higher-order functions.

```pycon exec="1" source="console" title="lambda.py"
>>> def factorial(n):
...    return reduce(lambda a, b: a*b, range(1, n+1))
>>> 
>>> from functools import reduce
>>> from operator import mul

>>> def factorial(n):
...    return reduce(mul, range(1, n+1))
```

List of public functions defined in `operator` and `functools`:

```pycon exec="1" source="console" title="lambda.py"
>>> import operator
>>> print([name for name in dir(operator) if not name.startswith('_')])
>>>
>>> import functools
>>> print([name for name in dir(functools) if not name.startswith('_')])
```

## Examples

### Itemgetter and Attrgetter

`itemgetter` and `attrgetter` are factories that pick items from sequences or read attributes from object.

`itemgetter` uses the `[]` operator, it supports not only sequences but also mappings and any class that implements `__getitem__`;

```pycon exec="1" source="console" title="lambda.py"
>>> metro_data = [
...     ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
...     ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
...     ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
... ]
>>>
>>> from operator import itemgetter
>>> for city in sorted(metro_data, key=itemgetter(1)):
...     print(city)

>>> cc_name = itemgetter(1, 0)
>>> for city in metro_data:
...     print(cc_name(city))
```

`attrgetter` creates functions to `extract object attributes by name`. `attrgetter` can navigate through nested objects that contains a .(dot), to retrieve the attribute.

```pycon exec="1" source="console" title="lambda.py"
>>> metro_data = [
...     ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
...     ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
...     ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
... ]
>>> 
>>> from collections import namedtuple
>>> LatLon = namedtuple('LatLon', 'lat lon')  
>>> Metropolis = namedtuple('Metropolis', 'name cc pop coord')  
>>> metro_areas = [Metropolis(name, cc, pop, LatLon(lat, lon))  
...     for name, cc, pop, (lat, lon) in metro_data]
>>> print(metro_areas[0])
>>>
>>> from operator import attrgetter
>>> name_lat = attrgetter('name', 'coord.lat') 
>>> for city in sorted(metro_areas, key=attrgetter('coord.lat')):  
...     print(name_lat(city))
```

### Methodcaller

Creates a function that calls a method by name on the object  given as argument.

```pycon exec="1" source="console" title="lambda.py"
>>> from operator import methodcaller
>>> s = 'The time has come'
>>> upcase = methodcaller('upper')
>>> print(upcase(s))
>>> hyphenate = methodcaller('replace', ' ', '-')
>>> print(hyphenate(s))
```

### Partial freezing arguments

Given a callable, it produces a new callable with some of the arguments of the original `callable bound to predetermined values`. `partial` takes a callable as first argument, followed by an arbitrary number of positional and keyword arguments to bind. The `functools.partialmethod` function does the same job as partial, but is designed to work with `methods`.

```pycon exec="1" source="console" title="lambda.py"
>>> from operator import mul
>>> from functools import partial
>>> triple = partial(mul, 3)
>>> print(triple(7))
>>> result = list(map(triple, range(1, 10)))
>>> print(result)
```

## References

- [Fluent Python, 2nd Edition](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/)
