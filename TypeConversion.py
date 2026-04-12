#type conversion : Type conversion, also known as type casting, is the process of converting a value from one data type to another. In Python, there are two types of type conversion: implicit and explicit.

a = 10
b = 3.14

# implicit type conversion
result = a + b  # a is converted to float
print("Result of a + b (implicit conversion):", result)

# explicit type conversion
result_explicit = a + int(b)  # b is explicitly converted to int    
print("Result of a + int(b) (explicit conversion):", result_explicit)
# converting to string
str_a = str(a)
print("String representation of a:", str_a)

# converting to float
float_a = float(a)  
print("Float representation of a:", float_a)

#type casting can also be used to convert between different data types, such as lists, tuples, and sets.

a = int("123")  # converting string to integer
print("Integer value of '123':", a) 
print("Type of a:", type(a))