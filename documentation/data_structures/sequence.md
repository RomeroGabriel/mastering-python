# Built-In Sequences

Python provides various built-in sequence types implemented in C, offering a rich set of functionalities through their APIs. These sequences include lists, tuples, strings, and range objects, each with its own unique features and use cases.

## Classifications/Types of Sequences

### Container x Flat

Container sequences, such as lists, tuples, and collections.deque, `can hold items of different types`, including other nested containers. They `hold references to the objects they contain`, which may be of any type.

On the other hand, flat sequences, like str, bytes, and array.array, `hold items of one simple type and store the value of their contents in their own memory space`, not as separate Python objects. Refer to the image below for more details.

![Container x Flat. Image from Fluent Python, 2nd Edition](https://raw.githubusercontent.com/RomeroGabriel/mastering-python/main/documentation/images/data_structures/containerVSflat.png)
> Container x Flat. Image from Fluent Python, 2nd Edition

## Mutable x Immutable

Mutable sequences include list, bytearray, array.array, and collections.deque. These sequences `can be modified after creation`, allowing you to add, remove, or modify elements.

Immutable sequences include tuple, str, and bytes. Once created, these sequences `cannot be changed`, meaning their elements cannot be modified or added.

`Mutable sequences inherit all methods from immutable sequences` and also implement several additional methods. Refer to the image below for more details.

![Mutable Inherit. Image from Fluent Python, 2nd Edition](https://raw.githubusercontent.com/RomeroGabriel/mastering-python/main/documentation/images/data_structures/mutable_inherit.png)
> Mutable Inherit. Image from Fluent Python, 2nd Edition
