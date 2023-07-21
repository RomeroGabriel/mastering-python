# Anonymous/Lambda Functions

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
