# print number from 1 to 100

i=1
while i <= 100:
    print(i)
    i += 1

# print numbers from 100 to 1

for i in range(100, 0, -1):
    print(i)

# print the elements of the following list using loop

list = [1,4,9,16,25]
for i in list:
    print(i)
# or

for i in range(len(list)):
    print(list[i])

# search for a number x in this tuple using loop

tuple = (1,4,9,16,25)
x = int(input("Enter a number to search: "))
found = False

for i in tuple:
    if i == x:
        print("Number found in the tuple.", i)
        found = True
        break
