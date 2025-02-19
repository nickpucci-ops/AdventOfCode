#day3
from utils import read_lines_from_file

list_of_rucksacks = read_lines_from_file("acday3.txt")

#print(list_of_rucksacks

def find_share_item(group):
    #half = int(len(rucksack)/2)
    #first = rucksack[:half]
    #second = rucksack[half:]
    share = ''.join(set.intersection(*map(set, group)))
    #share = ''.join(set(first).intersection(second))
    print(share)
    return share

def get_priority_value(rucksack, share):
    asc = ord(share)
    if share == share.lower():
        priority = asc-96
        #print(f"{share} : {priority}")
        #total += priority
    else:
        priority = asc-38
        #print(f"{share} : {priority}")
        #total += priority
    return priority

def grouper(my_list, group_size):
    return (my_list[i:i+group_size] for i in range(0, len(my_list), group_size))

total = 0

for group in grouper(list_of_rucksacks, 3):
    share = find_share_item(group)
    priority = get_priority_value(group, share)
    #for rucksack in group:
    #    priority = get_priority_value(rucksack, share)
    #    print(f"{rucksack}: {share} {priority}")
    total += priority
    print(total)
