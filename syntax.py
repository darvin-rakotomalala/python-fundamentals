"""
Python syntax is like grammar for this programming language.
Syntax refers to the set of rules that defines how to write and
organize code so that the Python interpreter can understand and
run it correctly. These rules ensure that your code is structured,
formatted, and error-free.
"""

"""
Python Indentation refers to the use of whitespace (spaces or tabs) at the beginning 
of code line. It is used to define the code blocks. Indentation is crucial in Python 
because, unlike many other programming languages that use braces "{}" to define blocks, 
Python uses indentation. It improves the readability of Python code, but on other hand 
it became difficult to rectify indentation errors. Even one extra or less space 
can leads to indentation error.
"""

print("-----------------------------------------")
print("- Indentation example")
if 10 > 5:
    print("This is true!")
    print("I am tab indentation")

print("I have no indentation")

print("-----------------------------------------")

"""
Variables in Python are essentially named references pointing to objects in memory. 
Unlike some other languages, you don't need to declare a variable's type 
explicitly in Python. Based on the value assigned, Python will dynamically determine the type. 
"""
print("- Python Variables example")

a = 10
print(type(a))

b = 'RakDa-Dev'
print(type(b))

print("-----------------------------------------")
"""
In Python, identifiers are unique names that are assigned to variables, 
functions, classes, and other entities. 
"""
print("- Python Identifiers example")
first_name = "Darvin Rakotomalala"
print(first_name)

print("-----------------------------------------")

"""
Keywords in Python are reserved words that have special meanings and serve 
specific purposes in the language syntax.
They cannot be used as identifiers (names for variables, functions, classes, etc.). 
For instance, "for", "while", "if", and "else" are keywords and cannot be used as identifiers.

False       await       else       import       pass  
None        break       except     in           raise 
True        class       finally    is           return
and         continue    for        lambda       try  
as          def         from       nonlocal     while
assert      del         global     not          with  
async       elif        if         or           yield
"""

print("- Comments in Python")
print("- Python Single Line Comment example")
first_name = "Darvin"
last_name = "Rakotomalala"  # assign last name

# print full name
print(first_name, last_name)

print("- Python Multi-Line Comment example")
'''
Multi Line comment.
Code will print name.
'''

f_name = "Tojo Darvin"
print(f_name)

print("-----------------------------------------")
"""
In Python, you can break a statement into multiple lines using the backslash. 
This method is useful, especially when we are working with strings or mathematical operations.
"""
print("- Multiple Line Statements - Using Backslashes")

sentence = "This is a very long sentence that we want to " \
           "split over multiple lines for better readability."

print(sentence)

# For mathematical operations
total = 1 + 2 + 3 + \
        4 + 5 + 6 + \
        7 + 8 + 9

print(total)

print("-----------------------------------------")

"""
In Python, statements are typically written on a single line. However, there are 
scenarios where writing a statement on multiple lines can improve readability or 
is required due to the length of the statement.
"""
print("- Continuation of Statements in Python")
print("- Implicit Continuation example")
# Line continuation within square brackets '[]'
numbers = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]

print(numbers)

print("- Explicit Continuation example")
# Explicit continuation using backslash '\'
s = "RakDa-Dev is computer science portal " \
    "by Darvin, used by Rakotomalala."

print(s)

print("-----------------------------------------")

