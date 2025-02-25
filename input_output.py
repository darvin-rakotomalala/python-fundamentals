"""
Understanding input and output operations is fundamental to Python programming.
With the print() function, we can display output in various formats,
while the input() function enables interaction with users by gathering
input during program execution.
"""
print("-------------------------------------------------")
print("Hello, World!")

print("- Printing Variables example")
# Single variable
s = "Darvin"
print(s)

# Multiple Variables
s = "Rakotomalala"
age = 25
city = "Madagascar"
print(s, age, city)

print("- Output Formatting example")
## Example 1: Using Format()
amount = 150.75
print("Amount: ${:.2f}".format(amount))

## Example 2: Using sep and end parameter
# end Parameter with '@'
print("Python", end='@')
print("DarvinDev")

# Separating with Comma
print('G', 'F', 'G', sep='')

# for formatting a date
print('09', '12', '2016', sep='-')

# another example
print('pratik', 'DarvinDev', sep='@')

## Example 3: Using f-string
name = 'Darvin'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.")

"""
Example 4: Using % Operator:
- %d –integer
- %f – float
- %s – string
- %x –hexadecimal
- %o – octal
"""
# Taking input from the user
# num = int(input("Enter a value: "))
num = 30
add = num + 5
# Output
print("The sum is %d" % add)

## Take Multiple Input in Python
print("- Take Multiple Input examples")
"""
print("- Taking two inputs at a time")
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
"""

"""
print("- Taking three inputs at a time")
x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)
"""

"""
## Take Conditional Input from user
print("- Take Conditional Input from user")
# Prompting the user for input
age_input = input("Enter your age: ")

# Converting the input to an integer
age = int(age_input)

# Checking conditions based on user input
if age < 0:
    print("Please enter a valid age.")
elif age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
"""

"""
print("- Taking input example")
name = input("Enter your name: ")
print("Hello,", name, "! Welcome!")
"""

print("- Find DataType of Input")
a = "Hello World"
b = 10
c = 11.22
d = ("Rak", "for", "Da")
e = ["Rak", "for", "Da"]
f = {"Darvin": 1, "for": 2, "Dev": 3}

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
