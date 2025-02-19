import os

"""
Read input from test cases
"""

def read_lines_from_file(filename):
    with open(filename, "r") as my_file:
        return my_file.read().splitlines()

#filename = input("Enter filename: ")
#print(f"Looking for {filename}")
#if os.path.exists(filename):
#     for line in read_lines_from_file(filename):
#         print(line)
#else: print(f"Could not find {filename}")

#for line in read_lines_from_file("names.txt"):
#    print(line)

#print(f"List of groceries: {read_lines_from_file('groceries.txt')}")

#read_lines_from_file("groceries.txt")
