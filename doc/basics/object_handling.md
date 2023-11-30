# Object References, Mutability, and Recycling

## Variables references

In Python, **variables serve as labels that refer to objects** stored in memory. It's important to understand that **an object can have multiple labels assigned to it**, creating a form of aliasing. Instead of saying that an object is assigned to a variable, **it is more accurate and meaningful to say that a variable is assigned to an object**. This shift in perspective acknowledges that the object exists before the assignment takes place, clarifying the relationship between variables and objects.

If a variable **changes the value of an object, all other variables assigned to the same object will reflect** that change as well.

```pycon exec="1" source="console" title="var_ref.py"
>>> a = [1, 2, 3] 
>>> b = a          
>>> a.append(4)    
>>> print(b)
>>> print(a)
```

![Object references. Image from Fluent Python, 2nd Edition](https://raw.githubusercontent.com/RomeroGabriel/mastering-python/main/documentation/images/basics/objec_ref.png)

## Identity and Equality

In Python, variables that refer to the **same object have the same identity and values**. Any changes made to the object through one variable will be reflected when accessing it through the other variable.

On the other hand, if **two different objects are created with the same values**, they will have **different identities**. This is because **each object occupies a distinct location in memory**, even though their values may be the same. It's important to note that **equality of values does not imply identity**. Each object has its own unique identity, regardless of the similarity of their values.

```pycon exec="1" source="console" title="identity_equality.py"
>>> charles = {'name': 'Charles L. Dodgson', 'born': 1832}
>>> lewis = charles  
>>> print(f"Lewis is charles? {lewis is charles}")
>>> print(f"Charles id: {id(charles)}, Lewis id: {id(lewis)}")
>>> lewis['balance'] = 950  
>>> print(f"Charles with balance property also {charles}")

>>> alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
>>> print(f"Alex == Charles? {alex == charles}")
>>> print(f"Alex is Charles? {alex is charles}")
```

## Choosing between `==` and `is`

In Python, the **== operator is used to compare the values of objects**, evaluating whether they hold the same data. On the other hand, the **is operator compares the identities of objects**, determining if they refer to the same underlying object in memory.

The **is** operator is generally **faster than == because it cannot be overloaded**. Since it is not subject to method invocations, P**ython can directly compare the integer IDs of the objects**, making the evaluation process straightforward and efficient. In contrast, when using the **==** operator, Python invokes the `__eq__()` special method to compare the values of objects. This syntactic sugar allows for more flexible value comparisons and supports custom equality behavior defined by the objects' classes.

## Copying objects

In Python, there are two types of object copying: *deep* copy and *shallow* copy.

A *deep* copy **creates a completely independent duplicate of an object**, including any nested objects it may contain. This means that the duplicate object and its nested objects **do not share any references with the original object**. Any modifications made to the duplicate will not affect the original object or its nested objects.

On the other hand, a *shallow* copy creates a new object that **shares some references with the original object**. It essentially creates a new object with a **separate identity, but certain internal references are still shared**. This means that changes made to the shallow copy may impact the original object or its nested objects, as they are still connected through shared references.

**By default, Python performs shallow copies** when creating copies of objects. However, it's important to note that some built-in data types, such as numbers and strings, are immutable, and creating copies of them behaves like a deep copy, as there are no nested mutable objects to share references with.

```pycon exec="1" source="console" title="copy.py"
>>> l1 = [3, [66, 55, 44], (7, 8, 9)]
>>> l2 = list(l1)
>>> print(f"l1 == l2? {l1 == l2}")
>>> print(f"l1 is l2? {l1 is l2}")
>>> print(f"l1 id: {id(l1)}, l2 id: {id(l2)}")
>>> l1.append(100)
>>> print("You can change l1 just fine, without changing l2: ")
>>> print(l1)
>>> print(l2)
>>> print("However, when you change l1[1], and l2[1] which is a list and mutable")
>>> l1[1].remove(55)   
>>> l2[1] += [33, 22]  
>>> l2[2] += (10, 11)
>>> print(l1)
>>> print(l2)
```

In Python, you have the ability to customize the behavior of copying objects by implementing the `__copy__()` and `__deepcopy__()` special methods.

The `__copy__()` method allows you to **define how an object should be shallow copied**. By *overriding this method in your class*, you can specify the exact behavior you desire when creating a shallow copy of an instance. Similarly, the `__deepcopy__()` method allows you to **define the behavior for deep copying an object**. By implementing this method, you can control how the object and its nested objects should be duplicated to create an independent deep copy.

## Command `del` and Garbage Collection

> Objects are never explicitly destroyed; however, when they become unreachable they
may be garbage-collected.

The `del` is that it’s not a function, it’s a statement. del deletes references, not objects. Python’s garbage collector may discard an object from memory as an indirect result of del, if the deleted variable was the last reference to the object. In CPython, the primary algorithm for garbage collection is reference counting.

```pycon exec="1" source="console" title="del.py"
>>> a = [1, 2]  
>>> b = a
>>> print(id(a), id(b))
>>> del a
>>> print(b)
>>> print("Rebinding b to a different object, removing the last remaining reference to [1, 2]")
>>> b = [3]
>>> print(id(b))
>>> print("Now the garbage collector can discard that object.")
```

## References

- [Fluent Python, 2nd Edition](https://learning.oreilly.com/library/view/fluent-python-2nd/9781492056348/)
