# WAP to print the length of a list using a function.

def list_length(lst):
    count = 0
    for item in lst:
        count += 1
    return count

# WAP to print the elements of a list in a single line using a function.

def print_list(lst):
    for item in lst:
        print(item, end=" ")
    return 0

# WAP to find the factorial of n using a function.

def factorial (n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
    
print("The factorial of 5 is:", factorial(5))
# WAP to convert usd to inr using a function.

def converter(usd):
    return usd * 82.74

