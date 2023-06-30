# Variables and Data Types  

In Python, variables can refer to different types of data, enabling us to manipulate that data as needed. To facilitate this, Python offers a range of standard data types that are specifically designed for storing and manipulating various kinds of data.

## Variables

One of the most notable and distinct features of variables in Python is their dynamic typing. This means that a single variable can change its type as required during the execution of the program.

```pycon exec="1" source="console" title="variables.py"
>>> nice_var = 123
>>> print(type(nice_var))
>>> nice_var = "now I'm a string"
>>> print(type(nice_var))
```

## Data Types

Python categorizes data types into the following categories: Text, Numeric, Sequence, Mapping, Set, Boolean, and Binary types. These categories encompass the various types of data that Python can handle.

### Text Type

- **str**: Represents a sequence of characters, such as "hello" or "Python". **Strings are immutable.**

```pycon exec="1" source="console" title="text.py"
>>> string_var = "Corinthians please help me"
>>> print(string_var)
>>> print(type(string_var))
```

### Numeric Type

- **str**: Represents integers (whole numbers) like 5, -3, 100.
- **float**: Represents floating-point numbers with decimal places like 3.14, -0.5, 2.0.

```pycon exec="1" source="console" title="numeric.py"
>>> int_number = 1910
>>> print(int_number)
>>> print(type(int_number))
>>> print(int_number + 2)
>>> float_number = int_number + 0.3
>>> print(float_number)
>>> print(type(float_number))
```

### Sequence Type

- **list**: Represents an ordered collection of elements enclosed in square brackets ([]). Lists can contain elements of **different data types** and are **mutable**, meaning you can modify them.
- **tuple**: Similar to lists, tuples represent an ordered collection of elements enclosed in parentheses (()). However, tuples are **immutable**, meaning they cannot be modified once created.
- **range**: Python provides a built-in range() function that **generates a sequence of numbers** within a specified range. The range() function is commonly used in loops and iterations.

```pycon exec="1" source="console" title="sequence.py"
>>> my_list = list([1, 2, 3, 4])
>>> print(my_list)
>>> print(type(my_list))

>>> my_list = [5, 6, 7, 8]
>>> print(my_list)
>>> print(type(my_list))
>>> print("--------------------------->")

>>> my_tuple = (1, 2, 3, 4, 5)
>>> print(my_tuple)
>>> print(type(my_tuple))
>>> my_tuple = tuple((1, 2, 3, 4, 5)) # cannot tuple(1, 2, 3, 4, 5)
>>> print(my_tuple)
>>> print(type(my_tuple))
>>> print("Tuple with only one element")
>>> my_tuple = (1,) # or tuple((1,))
>>> print(my_tuple)
>>> print(type(my_tuple))
>>> print("--------------------------->")

>>> my_range = range(1, 5)
>>> for num in my_range:
>>>     print(f"num value: {num}")

```

### Mapping Type

- **dictionary (dict)**: Represents a collection of key-value pairs enclosed in curly braces ({}) or created using the dict() constructor. Dictionaries provide a way to store and retrieve data using unique keys.

```pycon exec="1" source="console" title="dict.py"
>>> my_dict = {"name" : "Gabriel", "age" : 25}
>>> print(my_dict)
>>> print(type(my_dict))

>>> my_dict = dict(name="Gabriel", age=25)
>>> print(my_dict)
>>> print(type(my_dict))
```

### Set Data Types

- **set**: Represents an **unordered collection of unique elements** enclosed in curly braces ({}) or created using the set() constructor. Sets are useful to perform **operations like union, intersection, and difference**.
- **fronzenset**: Similar to set, frozensets are **immutable** and represent an unordered collection of unique elements. While elements of a set can be modified at any time, **elements of the frozen set remain the same after creation**.

```pycon exec="1" source="console" title="set.py"
>>> my_set = set(("apple", "banana", "cherry"))
>>> print(my_set)
>>> print(type(my_set))

>>> my_set = {5, 6, 7, 8}
>>> print(my_set)
>>> print(type(my_set))
>>> print("--------------------------->")

>>> my_frozenset = frozenset([1, 2, 3, 4, 5])
>>> print(my_frozenset)
>>> print(type(my_frozenset))
```

### Boolean Type

- **boll**: Represents a logical value indicating either True or False. Boolean values are often the result of comparisons or logical operations.

```pycon exec="1" source="console" title="bool.py"
>>> my_bool = bool(5)
>>> print(my_bool)
>>> print(type(my_bool))
>>> my_bool = bool(0)
>>> print(my_bool)
>>> print(type(my_bool))
>>> my_bool = True
>>> print(my_bool)
>>> print(type(my_bool))
```

### Binary Types

- **bytes**: Bytes are **immutable sequences** of individual bytes. They represent a **fixed sequence of bytes that cannot be modified** once created. Bytes can be created using literals or by calling the built-in bytes() constructor. They are commonly used to s**tore and process raw binary data**.
- **bytearray**: Bytearray, unlike bytes, is a **mutable sequence** of bytes. It **allows modifications after creation**, such as appending, replacing, or deleting elements. Bytearray objects can be created using literals or by calling the bytearray() constructor. They provide a flexible way to **modify binary data**.
- **memoryview**: Memoryview is a Python object that provides a way to **access the internal data of an object** (such as bytes or bytearray) **without making a copy**. It acts as a "window" into the data, allowing **efficient access and manipulation of large amounts of binary data**. Memoryview objects can be created by calling the built-in memoryview() constructor.

```pycon exec="1" source="console" title="binary.py"
>>> my_bytes = b"Hello"
>>> print(my_bytes)
>>> print(type(my_bytes))
>>> my_bytes = bytes(5)
>>> print(my_bytes)
>>> print(type(my_bytes))
>>> print("--------------------------->")

>>> my_bytes = bytearray(5)
>>> print(my_bytes)
>>> print(type(my_bytes))
>>> print("--------------------------->")

>>> my_bytes = memoryview(bytes(5))
>>> print(my_bytes)
>>> print(type(my_bytes))
>>> print("--------------------------->")
```

### None Type

- **None**: Represents a special value indicating the absence of a value. It is commonly used to denote a variable that has not been assigned a value.

```pycon exec="1" source="console" title="none.py"
>>> my_none = None
>>> print(my_none)
>>> print(type(my_none))
```

## References

- [W3Schools - Python Data Types](https://www.w3schools.com/python/python_datatypes.asp)
