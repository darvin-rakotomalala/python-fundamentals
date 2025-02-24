"""
Variables are used to store data that can be referenced and manipulated
during program execution. A variable is essentially a name that is assigned to a value.
Python variables do not require explicit declaration of type. The type of the variable
is inferred based on the value assigned.
"""
print("----------------------------------------------------------")
# Variable 'x' stores the integer value 10
x = 5

# Variable 'name' stores the string "Samantha"
name = "Darvin Raktomalala"

print("- Variables example")
print(x)
print(name)

"""
Rules for Naming Variables
To use variables effectively, we must follow Python’s naming rules:
- Variable names can only contain letters, digits and underscores (_).
- A variable name cannot start with a digit.
- Variable names are case-sensitive (myVar and myvar are different).
- Avoid using Python keywords (e.g., if, else, for) as variable names.
"""

# Valid Example
age = 21
_colour = "lilac"
total_score = 90

# Invalid Example
"""
1name = "Error"  # Starts with a digit
class = 10       # 'class' is a reserved keyword
user-name = "Doe"  # Contains a hyphen
"""

# Assigning Values to Variables
# Basic Assignment using the = operator
x = 5
y = 3.14
z = "Hi"

# Dynamic Typing
x = 10
x = "Now a string"

# Multiple Assignment
# Assigning the Same Value
a = b = c = 100
print(a, b, c)
x, y, z = 1, 2.5, "Python"
print(x, y, z)

# Type Casting a Variable
"""
Basic Casting Functions
- int() – Converts compatible values to an integer.
- float() – Transforms values into floating-point numbers.
- str() – Converts any data type into a string.
"""
# Casting variables
s = "10"  # Initially a string
n = int(s)  # Cast string to integer
cnt = 5
f = float(cnt)  # Cast integer to float
age = 25
s2 = str(age)  # Cast integer to string

# Display results
print("- Examples of Casting")
print(n)
print(f)
print(s2)

# Getting the Type of Variable
# Define variables with different data types
n = 42
f = 3.14
s = "Hello, World!"
li = [1, 2, 3]
d = {'key': 'value'}
bool = True

# Get and print the type of each variable
print("- Example Usage of type()")
print(type(n))
print(type(f))
print(type(s))
print(type(li))
print(type(d))
print(type(bool))

# Scope of a Variable
# Local Variables
print("- Local Variables")


def func_local():
    a = "I am local"
    print(a)


func_local()

# Global Variables
"""
Variables defined outside any function are global and can be 
accessed inside functions using the global keyword.
"""
print("- Global Variables")
a = "I am global"


def func_global():
    global a
    a = "Modified globally"
    print(a)


func_global()
print(a)

# Object Reference in Python
"""
Key Takeaways:
- Python variables hold references to objects, not the actual objects themselves.
- Reassigning a variable does not affect other variables referencing the same 
object unless explicitly updated.
"""

# Delete a Variable Using del Keyword
print("- Delete a Variable Using del Keyword")
# Assigning value to variable
x = 10
print(x)

# Removing the variable using del
del x
# Trying to print x after deletion will raise an error
# print(x)  # Uncommenting this line will raise NameError: name 'x' is not defined

# Practical Examples
print("- Practical Examples")
print("- Swapping Two Variables")
a, b = 5, 10
a, b = b, a
print(a, b)

print("- Counting Characters in a String")
word = "Python"
length = len(word)
print("Length of the word:", length)

