# Higher-Order Functions

A function is classified as a Higher Order Function (HOF) when it `takes other functions as parameters or returns a function as its output`. In other words, HOFs are functions that interact with other functions.
Common examples of HOFs include map, filter, and reduce. These functions accept any one-argument function as a key.

Key properties of higher-order functions:

1. Functions are instances of the Object type.
1. Functions can be stored in variables.
1. Functions can be passed as parameters to other functions.
1. Functions can be returned from a function.
1. Functions can be stored in data structures like hash tables and lists.

```pycon exec="1" source="console" title="lambda.py"
>>> fruits = ['banana', 'apple', 'fig', 'strawberry', 'cherry', 'raspberry']
>>> def reverse(word):
...     return word[::-1]
>>> print(reverse('testing'))
>>> print(list(map(reverse, fruits)))
```

## References

- [Geeks for Geeks - Higher Order Functions in Python](https://www.geeksforgeeks.org/higher-order-functions-in-python/)
