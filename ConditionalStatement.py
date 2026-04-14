# Conditional statement

# A conditional statement is a statement that performs different actions based on different conditions. In Python, we use the if statement to create a conditional statement.

# if-elif-else statement

# The if-elif-else statement is used to check multiple conditions. It allows you to execute different blocks of code based on different conditions.

# if condition1:
#     # code to execute if condition1 is true   
# elif condition2:
#     # code to execute if condition2 is true
# else:
#     # code to execute if both condition1 and condition2 are false


age = 18

if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You are just an adult.")
else:
    print("You are an adult.")

# Output: You are just an adult.