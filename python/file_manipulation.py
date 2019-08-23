#!/usr/bin/env python

"""file_manipulation.py: Open, read and write to file examples."""

__author__      = "Mabboum"

filename = "file.txt"

# Open file to read only
def openReadFile():
    return open(filename, 'r')

# Open file to write
def openWriteFile():
    return open(filename, 'w')

# Open file to append
def openAppendFile():
    return open(filename, 'a')

# Read all lines of a file
def readAllFile():
    file = openReadFile()
    print(file.read())

# Read one line of a file, most likely to use in a loop
def readOneLineAtTime():
    file = openReadFile()
    print(file.readline())

# Read a file and add all lines to a list
def readLinesToList():
    file = openReadFile()
    print(file.readlines())

#  Write to a file
def writeToFile():
    file = openWriteFile()
    file.write("A new line")
    file.close()

# Write a list to a file
def writeListToFile():
    file = openWriteFile()
    lines_of_text = ["First sentence.", "Second sentence.", "Third sentence."]
    file.writelines(lines_of_text)
    file.close()
