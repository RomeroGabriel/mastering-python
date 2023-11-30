# Iterators

Iteration is a fundamental aspect of data processing in which programs `apply computations to data series`. When dealing with `data that doesn't fit into memory`, the need arises to fetch i`tems lazily—one at a time and on demand`. This is precisely the role of an iterator.

In Python, `every standard collection is iterable`. `An iterable is an object that offers an iterator`, a mechanism Python utilizes to facilitate operations such as:

1. `for` loops
1. List, dict, and set comprehensions
1. Unpacking assignments
1. Construction of collection instances

## The iter Function
