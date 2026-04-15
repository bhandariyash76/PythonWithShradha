# tuples in python are immutable sequences, meaning that once a tuple is created, its elements cannot be modified. They are defined using parentheses () and can contain elements of different data types.

# Creating a tuple
my_tuple = (1, "Hello", 3.14, True)

# Accessing elements in a tuple
print(my_tuple[0])  # Output: 1
print(my_tuple[1])  # Output: Hello
print(my_tuple[2])  # Output: 3.14
print(my_tuple[3])  # Output: True
 
# tuples slicing    
print(my_tuple[1:3])  # Output: ('Hello', 3.14)

# Tuples methods

print(my_tuple.index("Hello"))  # Output: 1
print(my_tuple.count(3.14))  # Output: 1

# Tuples can also be nested, meaning that a tuple can contain other tuples as elements.
nested_tuple = (1, (2, 3), 4)   