# File I/O in python: python can read and write files. It can also create new files and delete existing files.

#types of files: text files, binary files, csv files, json files, xml files, etc.
#binary files: files that contain data in a format that is not human-readable. They are used to store data that is not meant to be read by humans, such as images, videos, audio files, etc.

# basic operations on files: open, read, write, close, etc.

f = open("file.txt", "w") # open a file in write mode
f.write("Hello, World!") # write to the file
f.close() # close the file
f = open("file.txt", "r") # open a file in read mode
content = f.read() # read the content of the file   
print(content) # print the content of the file
f.close() # close the file
