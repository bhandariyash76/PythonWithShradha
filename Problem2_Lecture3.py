# WAP to count the number of students with the "A" grade in the following tuple

tuple_of_grades = ("A", "B", "C", "A", "D", "A", "B")

count_a_grade = tuple_of_grades.count("A")
print("number of students with A grade: ", count_a_grade)

# or we can use loop to count the number of students with A grade

count_a_grade = 0
for grade in tuple_of_grades:
    if grade == "A":
        count_a_grade += 1

print("number of students with A grade: ", count_a_grade)