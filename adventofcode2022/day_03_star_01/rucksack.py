import string
with open('pythonstuff/adventofcode2022/day_03_star_01/rucksack.txt') as inputfile:
    sum = 0
    for line in inputfile:
        midpoint = len(line) // 2
        #returns length of object and divides by two (rucksack item and compartment)
        first_half, second_half = line[:midpoint], line[midpoint:].strip()
        sum += int(string.ascii_letters.index(''.join(set(first_half).intersection(second_half)))) + 1
    print(sum)

