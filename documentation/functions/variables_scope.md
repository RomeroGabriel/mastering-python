# Variables Scope

Taking as example, this code:

```pycon exec="1" source="console"  title="var_scope.py"
>>> num = 2
>>> def var_scope(num_fun):
...     print(num_fun)
...     try:
...         print(num)
...         num = 10
...     except BaseException as err:
...         print(err)
...
>>> var_scope(5)
```

You may notice that `print(num_fun)` was executed successfully, while `print(num) raised an exception`, even though `num was initialized outside the function`. The reason behind this is that when Python compiles the function's body, `it identifies num as a local variable because it gets assigned within the function`. So, when the function `var_scope is called`, it can access and print the value of the local variable `num_fun`. However, when it attempts to access the `local variable num, it encounters an issue because b is not bound`.

In Python, there's `no requirement to declare variables explicitly`, but the `interpreter assumes that a variable assigned within a function is local`. If you want the interpreter to treat b as a global variable and still assign a new value to it within the function, you need to use the global declaration.

```pycon exec="1" source="console"  title="var_scope_global.py"
>>> num = 2
>>> def var_scope(num_fun):
...     global num
...     print(num_fun)
...     try:
...         print(num)
...         num = 10
...     except BaseException as err:
...         print(err)
...
>>> var_scope(5)
>>> print(num)
```

## Types of Scope

1. ??? info "Module Global Scope"
    Made of names assigned to values `outside of any class or function block`.
1. ??? info "Function Local Scope"
    Made of names assigned to values as `parameters, or directly in the body of the function`.
1. ??? info "Nonlocal Scope"
    The nonlocal scope refer to all those variables that are `declared within nested functions`. The `nonlocal keyword is used to work with variables inside nested functions`, where the variable should not belong to the inner function. It lets you declare a variable as a `free variable`.

## Variable Lookup Logic

## Comparing bytecodes

```pycon exec="1" source="console"  title="bytecodes_compare.py"
>>> num = 2
>>> def var_scope_right(num_fun):
...     global num
...     print(num_fun)
...     try:
...         print(num)
...         num = 10
...     except BaseException as err:
...         print(err)
...
>>> def var_scope_wrong(num_fun):
...     print(num_fun)
...     try:
...         print(num)
...         num = 10
...     except BaseException as err:
...         print(err)
...
>>> from dis import dis
>>> print(dis(var_scope_right)) # Don't know why is not working
>>> dis(var_scope_wrong) # Don't know why is not working
```

## References

- [Fluent Python, 2nd Edition](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/)
- [Python - 4.8. More on Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions)
- [Python nonlocal Keyword](https://www.w3schools.com/python/ref_keyword_nonlocal.asp)
