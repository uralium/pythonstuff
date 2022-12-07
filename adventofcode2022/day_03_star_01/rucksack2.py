import string

if __name__ == '__main__':
    with open('pythonstuff/adventofcode2022/day_03_star_01/rucksack.txt') as inputfile:
        sum = 0
        lines = inputfile.readlines()
        for i in range(0, len(lines), 3):
            sum += int(string.ascii_letters.index(''.join(set(lines[i].strip()).intersection(lines[i+1].strip()).intersection(lines[i+2].strip())))) + 1
        print(sum)