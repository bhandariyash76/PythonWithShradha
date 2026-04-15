# Lists in python : a built in data structure that can hold an ordered collection of items, which can be of different types. Lists are mutable, meaning you can change their content after they have been created.

# Creating a list

my_list = [1, 2, 3, 'hello', True] # list can contain different types of data

# Accessing elements in a list
print(my_list[0]) # Output: 1
print(my_list[3]) # Output: 'hello'
print(my_list)
print(type(my_list)) # Output: <class 'list'>

student = ['John', 20, 'Computer Science', 3.5]

# List slicing
print(student[0:2]) # Output: ['John', 20]
print(student[2:]) # Output: ['Computer Science', 3.5]
print(student[:3]) # Output: ['John', 20, 'Computer Science']

# in this we also have negative indexing which allows us to access elements from the end of the list
print(student[-1]) # Output: 3.5

# Modifying a list
student[1] = 21 # changing the age from 20 to 21
print(student) # Output: ['John', 21, 'Computer Science', 3.5]

# List methods

list1 = [1, 2, 3]
list1.append(4) # adds 4 to the end of the list
print(list1) # Output: [1, 2, 3, 4]

list1.sort() # sorts the list in ascending order
print(list1) # Output: [1, 2, 3, 4]

list1.append(9) # adds 9 to the end of the list
print(list1) # Output: [1, 2, 3, 4, 9]

list1.reverse() # reverses the order of the list
print(list1) # Output: [9, 4, 3, 2, 1]

list1.sort(reverse=True) # sorts the list in descending order
print(list1) # Output: [9, 4, 3, 2, 1]

list1.insert(2, 5) # inserts 5 at index 2
print(list1) # Output: [9, 4, 5, 3, 2, 1]

list1.remove(4) # removes the first occurrence of 4 from the list
print(list1) # Output: [9, 5, 3, 2, 1]

list1.pop(2) # removes and returns the item at index 2
print(list1) # Output: [9, 5, 3, 2, 1]

list1.pop() # removes and returns the last item from the list
print(list1) # Output: [9, 5, 3, 2]