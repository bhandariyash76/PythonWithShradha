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

#'r' - read mode: opens a file for reading. The file pointer is placed at the beginning of the file. This is the default mode.
#'w' - write mode: opens a file for writing. If the file already exists, it will be truncated to zero length. If the file does not exist, it will be created.
#'a' - append mode: opens a file for appending. The file pointer is placed at the end of the file. If the file does not exist, it will be created.
#'x' - exclusive creation mode: opens a file for exclusive creation. If the file already exists, the operation will fail.
#'+' - update mode: opens a file for updating (reading and writing). The file pointer is placed at the beginning of the file. If the file does not exist, it will be created.
#'b' - binary mode: opens a file in binary mode. This is used for files that contain data in a format that is not human-readable, such as images, videos, audio files, etc.
#'text' - text mode: opens a file in text mode. This is the default mode. It is used for files that contain data in a format that is human-readable, such as text files, csv files, json files, xml files, etc.

data = f.read(5) # read the content of the file
print(data) # print the content of the file
f.close() # close the file

data = f.readline() # read a line from the file
print(data) # print the line read from the file

