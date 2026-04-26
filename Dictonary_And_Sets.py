# Dictonary in python : used to store data in key value pair
# it is mutable and unordered collection of data

# creating a dictonary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(my_dict)

print(my_dict["name"])  # accessing value using key

my_dict["age"] = 31  # updating value
print(my_dict)

my_dict["country"] = "USA"  # adding new key-value pair
print(my_dict)

# Nested dictonary
nested_dict = {
    "person1": {
        "name": "John",
        "age": 30
    },
    "person2": {
        "name": "Jane",
        "age": 25
    }
}

print(nested_dict)

# Methods of dictonary
print(my_dict.keys())  # returns all keys
print(my_dict.values())  # returns all values
print(my_dict.items())  # returns all key-value pairs
print(my_dict.get("name"))  # returns value for the given key
print(my_dict.pop("age"))  # removes the key and returns its value
print(my_dict.update({"age": 31, "country": "USA"}))  # updates the dictonary with new key-value pairs
print(my_dict)

# Sets in python : used to store unique elements
# it is mutable and unordered collection of data

# creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)
print(len(my_set))  # length of the set

# Creating empty set
empty_set = set()
print(empty_set)

#methods of set
my_set.add(6)  # adding an element to the set
print(my_set)
my_set.remove(3)  # removing an element from the set
print(my_set)
my_set.discard(4)  # removing an element from the set without raising an error if it does not exist
print(my_set)
my_set.clear()  # removing all elements from the set
print(my_set)
my_set = {1, 2, 3, 4, 5}
my_set.pop()  # removing and returning an arbitrary element from the set
print(my_set)

print(set.union({1, 2, 3}, {3, 4, 5}))  # returns a new set with all unique elements from both sets
print(set.intersection({1, 2, 3}, {3, 4, 5}))  # returns a new set with only the elements that are common to both sets
print(set.difference({1, 2, 3}, {3, 4, 5}))  # returns a new set with only the elements that are in the first set but not in the second set
print(set.symmetric_difference({1, 2, 3}, {3, 4, 5}))
  # returns a new set with only the elements that are in either set but not in both sets
