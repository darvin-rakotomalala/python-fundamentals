"""
In Python programming, Operators in general are used
to perform operations on values and variables.
These are standard symbols used for logical and arithmetic operations.
    - OPERATORS: These are the special symbols. Eg- + , * , /, etc.
    - OPERAND: It is the value on which the operator is applied.

Types of Operators in Python
    - Arithmetic Operators
    - Comparison Operators
    - Logical Operators
    - Bitwise Operators
    - Assignment Operators
    - Identity Operators and Membership Operators
"""
print("-------------------------------------------------")

## Arithmetic Operators
print("- Example of Arithmetic Operators")
# Variables
a = 15
b = 4

# Addition
print("Addition:", a + b)

# Subtraction
print("Subtraction:", a - b)

# Multiplication
print("Multiplication:", a * b)

# Division
print("Division:", a / b)

# Floor Division
print("Floor Division:", a // b)

# Modulus
print("Modulus:", a % b)

# Exponentiation
print("Exponentiation:", a ** b)

## Comparison of Python Operators
print("- Example of Comparison Operators")
a = 13
b = 33

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

## Logical Operators
"""
The precedence of Logical Operators in Python is as follows:
    - Logical not
    - logical and
    - logical or
"""
print("- Example of Logical Operators")
a = True
b = False
print(a and b)
print(a or b)
print(not a)

## Bitwise Operators
"""
Bitwise Operators in Python are as follows:
    - Bitwise NOT
    - Bitwise Shift
    - Bitwise AND
    - Bitwise XOR
    - Bitwise OR
"""
print("- Example of Bitwise Operators")
a = 10
b = 4

# Print bitwise AND operation
print(a & b)

# Print bitwise OR operation
print(a | b)

# Print bitwise NOT operation
print(~a)

# print bitwise XOR operation
print(a ^ b)

# print bitwise right shift operator
print(a >> 2)

# print bitwise left shift operator
print(a << 2)

## Assignment Operators
print("- Example of Assignment Operators")
a = 10
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)

## Identity Operators
"""
In Python, is and is not are the identity operators both are used 
to check if two values are located on the same part of the memory. 
Two variables that are equal do not imply that they are identical. 
    - is      True if the operands are identical 
    - is not  True if the operands are not identical 
"""

print("- Example of Identity Operators")
a = 10
b = 20
c = a

print(a is not b)
print(a is c)

## Membership Operators
"""
In Python, in and not in are the membership operators that are used 
to test whether a value or variable is in a sequence.
    - in        True if value is found in the sequence
    - not in    True if value is not found in the sequence
"""

print("- Example of Membership Operators")
x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")

## Ternary Operator
"""
in Python, Ternary operators also known as conditional expressions 
are operators that evaluate something based on a condition being true or false.

It simply allows testing a condition in a single line replacing the multiline 
if-else making the code compact.
    Syntax :  [on_true] if [expression] else [on_false]
"""

print("- Example of Ternary Operator")
a, b = 10, 20
min = a if a < b else b

print(min)

## Precedence and Associativity of Operators
"""
In Python, Operator precedence and associativity determine the priorities of the operator.
"""
print("- Example of Operator Precedence")
"""
This is used in an expression with more than one operator with different 
precedence to determine which operation to perform first.
"""
expr = 10 + 20 * 30
print(expr)
name = "Alex"
age = 0

if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")
else:
    print("Good Bye!!")

print("- Example of Operator Associativity")
"""
If an expression contains two or more operators with the same 
precedence then Operator Associativity is used to determine. 
It can either be Left to Right or from Right to Left.
"""
print(100 / 10 * 10)
print(5 - 2 + 3)
print(5 - (2 + 3))
print(2 ** 3 ** 2)
