# High-Order and Lambda Function

## High-Order Functions

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

## Anonymous/Lambda Functions

Lambda functions can be used wherever function objects are required. They can only contain `pure expressions and cannot include other Python statements` like while, try, or assignment statements. Despite these limitations, lambda functions are semantically `equivalent to normal function definitions and act as syntactic sugar for them.` Lambda functions are commonly used when a simple, short function is required, and there's no need to define a full-fledged function using the def statement. Like nested function definitions, lambda functions can reference variables from the containing scope:

```pycon exec="1" source="console" title="lambda.py"
>>> def make_incrementor(n):
...    return lambda x: x + n
>>> f = make_incrementor(42)
>>> print(f(0))
>>> print(f(1))
```

```pycon exec="1" source="console" title="lambda2.py"
>>> fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
>>> print(sorted(fruits, key=lambda word: word[::-1]))
```

## References

- [Geeks for Geeks - Higher Order Functions in Python](https://www.geeksforgeeks.org/higher-order-functions-in-python/)
