# functions in python: block of statement that performs a specific task.

# syntax of function:
# def function_name(parameters):
#     statement(s)

# example of function:
def sum(a, b):
    return a + b

# calling the function:
result = sum(5, 10)
print("The sum is:", result)

# or

print("The sum is:", sum(5, 10))

# recursion: a function that calls itself.
# example of recursion:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# calling the recursive function:
print("The factorial of 5 is:", factorial(5))