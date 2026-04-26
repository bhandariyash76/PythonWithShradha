# wap to enter marks of 3 subjects from the user and store them in a dictionary. start with an empty sictionary & add one by one. use subject name as key & marks as value. finally print the dictionary.

# # create an empty dictionary to store subject marks
subject_marks = {}

# get marks for 3 subjects from the user and store in the dictionary

for i in range (3):
    subject = input("enter subject name:")
    marks = int(input("enter marks"))
    subject_marks[subject] = marks

# print the dictionary
print(subject_marks)


# figue out a way to store 9 & 9.0 as a separate values in set

# create a set to store values
values_set = set()
# add values to the set
values_set.add(int(9))
values_set.add(str(9.0))
# print the set
print(values_set)