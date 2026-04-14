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
    