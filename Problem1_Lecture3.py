# WAP to ask the user to enter names of their 3 favorite movies and store them in list

list_of_movies = list(map(str, input("enter names of movies separated by space: ").split()))

print("your favorite movies are: ", list_of_movies)


# WAP to check if a list contains a palimdrome of elements or not

def is_palindrome(lst):
    return lst == lst[::-1]

# OR we can use copy method to create a copy of the list and then reverse it and compare with original list

def is_palindrome(lst):
    lst_copy = lst.copy()
    lst_copy.reverse()
    return lst == lst_copy

# or we can use loop to check if the list is palindrome or not

def is_palindrome(lst):
    for i in range(len(lst)//2):
        if lst[i] != lst[len(lst)-1-i]:
            return False
    return True