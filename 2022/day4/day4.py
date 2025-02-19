#day 4
from utils import read_lines_from_file

list_of_pairs = read_lines_from_file("acday4.txt")
#print(list_of_pairs)

test_pair = list_of_pairs[999]
print(test_pair)

lst = test_pair.split("\n")
print(lst)

string = lst[0]
test = string[0]

print(test)

pair1 = 0
