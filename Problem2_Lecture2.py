# grade students based on marks 

marks = int(input("Enter the marks: "))

if marks >= 90:
    print("Grade: A")
elif 90 > marks >= 80:
    print("Grade: B")
elif 80 > marks >= 70:
    print("Grade: C")
elif 70 > marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")


# WAP to check if a number is even or odd

number = int(input("enter the number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# WAP to find the greatest of 3 numbers entered by the user

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    greatest = num1
elif num2 >= num1 and num2 >= num3:
    greatest = num2
else:   
    greatest = num3

print("The greatest number is:", greatest)

#WAP to check if a number is a multiplle of 7 or not

num = int(input("Enter a number: "))

if num % 7 == 0:
    print(num, "is a multiple of 7.")
else:
    print(num, "is not a multiple of 7.")