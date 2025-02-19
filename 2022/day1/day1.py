from utils import read_lines_from_file

list_of_calories = read_lines_from_file("aocDay1Input.txt")
list_of_elves = []
total_calories = 0
for calories in list_of_calories:
    if not calories.isdigit():
        list_of_elves.append(total_calories)
        total_calories = 0
        continue
    total_calories += int(calories)
list_of_elves.append(total_calories)
print(list_of_elves)

def get_and_remove_max_calories():
    max_calories = 0
    for elf in list_of_elves:
        if elf > max_calories:
            max_calories = elf
    print(f"max_calories: {max_calories}")
    list_of_elves.remove(max_calories)
    return max_calories

total = 0
for i in range(3):
    topElf = get_and_remove_max_calories()
    print(f"top elf: {topElf}")
    total += topElf

print(f"Final total: {total}")
