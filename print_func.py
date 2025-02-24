"""
The print() function is a fundamental part of Python that allows
for easy console output. The function has replaced the older print
statement in Python 3, providing more versatility with keyword arguments.
"""
from pprint import pprint

print("----------------------------------------------------------")
# Advanced String Formatting
name = "Darvin"
age = 32
print(f"Hello, {name}. You are {age} years old.")

# Using .format()
print("Hello, {}. You are {} years old.".format(name, age))

# Using % operator
print("Hello, %s. You are %d years old." % (name, age))

# Working with Quotes in Strings
"""
- Single Quotes: For simple strings: print('Hello')
- Double Quotes: Useful for strings with single quotes inside: print("Python's simplicity")
- Triple Quotes: Allow multi-line strings and embedded quotes
"""
print("- Triple Quotes example")
print("""Python is versatile.
It's also popular!""")

# Variable Use
print("- Variable Use - Example 1")
str1 = 'Wel'
print(str1, 'come')  # Output: Welcome

print("- Variable Use - Example 2")
str1 = 'Welcome'
str2 = 'Python'
print(str1, str2)

# String Concatenation
print("- String Concatenation - Example")
str1 = 'Python'
str2 = ':'
print('Welcome' + str1 + str2)

# Using as String
print("- Using as String - Example")
str1 = 'Python'
print("Welcome %s" % str1)

"""
Using other data types:
    %d -> Integer
    %e -> exponential
    %f -> Float
    %o -> Octal
    %x -> Hexadecimal
"""
print("- Using other data types example")
print("Actual Number = %d" % 15)
print("Exponential equivalent of the number = %e" % 15)
print("Float of the number = %f" % 15)
print("Octal equivalent of the number = %o" % 15)
print("Hexadecimal equivalent of the number = %x" % 15)

print("- Using multiple variables example")
str1 = 'World'
str2 = ':'
print("Python %s %s" % (str1, str2))

print("- Repeating Characters example")
print('#' * 10)  # Output: ##########

print("- Example - Line Break")
# \n is used for Line Break
print("Sunday\nMonday\nTuesday\nWednesday\nThursday\nFriday\nSaturday")

print("- Example - using tab")
# \t is used for tab
print("""
Language:
\t1 Python
\t2 Java\n\t3 JavaScript
""")

# Pretty Printing with pprint
print("- Pretty Printing with pprint")
data = {"Python": 3, "Java": 8, "C++": 11}
pprint(data)
