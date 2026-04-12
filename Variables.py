# variables : a container that holds a value. It is a way to store data in a program. In python, we can create a variable by assigning a value to it using the equal sign (=). The name of the variable should be descriptive and should not contain spaces or special characters.

#Rules for identifiers (variable names):
#1. Variable names must start with a letter or an underscore (_).
#2. Variable names can only contain letters, numbers, and underscores.
#3. Variable names are case-sensitive (age and Age are different variables).


# example of creating a variable

name = "yash bhandari" #string variable
age = 23 #integer variable
height = 5.8 #float variable

# in the above example, we have created three variables: name, age, and height. The variable name holds a string value, age holds an integer value, and height holds a float value.

print(name)
print(age)
print(height)

print("my name is " + name + " and I am " + str(age) + " years old.") 
#string concatenation 

#Data types:
#1. String: a sequence of characters enclosed in quotes. Example: "Hello, World!"
#2. Integer: a whole number without a decimal point. Example: 23
#3. Float: a number with a decimal point. Example: 5.8
#4. Boolean: a data type that can only have two values: True or False.
#5. None: a special data type that represents the absence of a value. It is often used to indicate that a variable has no value or that a function does not return anything. Example: None