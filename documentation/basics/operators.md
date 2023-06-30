# Python Operators

## Arithmetic Operators

- **Addition**: +
- **Subtraction**: -
- **Multiplication**: *
- **Division**: /
- **Floor Division**: //
- **Modulus**: %
- **Exponentiation**: **

```pycon exec="1" source="console" title="arith_operators.py"
>>> addition = 123 + 123
>>> subtraction = 123 - 123
>>> multi = 123 * 123
>>> division = 123 / 123
>>> floor_division = 25 // 5
>>> print(f"floor_division by 25/5: {floor_division}")
>>> floor_division = 25 // 6
>>> print(f"floor_division by 25/6: {floor_division}")
>>> modulus = 25 % 5
>>> print(f"modulus by 25/5: {modulus}")
>>> modulus = 25 % 6
>>> print(f"modulus by 25/6: {modulus}")
>>> exponentiation = 2 ** 2
>>> print(f"exponentiation: {exponentiation}")
```

## Assignment Operators

- **Assignment:** =
- **Addition Assignment**: +=
- **Subtraction Assignment**: -=
- **Multiplication Assignment**: *=
- **Division Assignment**: /=
- **Floor Division Assignment**: //=
- **Modulus Assignment**: %=
- **Exponentiation Assignment**: **=

## Comparison Operators

- **Equal to**: ==
- **Not equal to**: !=
- **Greater than**: >
- **Less than**: <
- **Greater than or equal to**: >=
- **Less than or equal to**: <=

## Logical Operators

- **Logical AND**: and
- **Logical OR**: or
- **Logical NOT**: not

## Bitwise Operators

Bitwise operators are used to perform operations on **individual bits of binary numbers**. They treat numbers as sequences of binary digits (bits) and operate on them bit by bit.

- **Bitwise AND**: &

    Performs a logical AND operation on each pair of corresponding bits. If both bits are 1, the result is 1. Otherwise, the result is 0.

- **Bitwise OR**: |

    Performs a logical OR operation on each pair of corresponding bits. If at least one bit is 1, the result is 1. Otherwise, the result is 0.

- **Bitwise XOR**: ^

    Performs a logical XOR (exclusive OR) operation on each pair of corresponding bits. If the two bits are different (one is 0 and the other is 1), the result is 1. Otherwise, the result is 0.

- **Bitwise NOT**: ~

    Inverts (flips) the bits of a number. Changes each 1 to 0 and each 0 to 1.

- **Left Shift**: <<

    Shifts the bits of a number to the left by a specified number of positions. The empty positions on the right are filled with zeros. Each shift to the left is equivalent to multiplying the number by 2.

- **Right Shift**: >>

    Shifts the bits of a number to the right by a specified number of positions. The empty positions on the left are filled with the sign bit (0 for positive numbers, 1 for negative numbers). Each arithmetic shift to the right is equivalent to dividing the number by 2.

Bitwise operators are commonly used in **low-level programming, networking, and manipulation of binary data**. They allow you to manipulate individual bits within numbers, set or clear specific flags, or extract information from bit patterns.

## Membership Operators

- **In**: in
- **Not in**: not in

## Identity Operators

- **Is**: is
- **Is not**: is not

## Unary Operators

- **Positive**: +
- **Negative**: -
- **Logical NOT**: not

## Ternary Operator

- **Conditional Expression**: a if condition else b

```pycon exec="1" source="console" title="ternary.py"
>>> a = 10
>>> b = 20
>>> print(a if a > b else b)
```
