       
scores_part_1 = {
    "A": {
        "X": 4,
        "Y": 8,
        "Z": 3
    },
    "B": {
        "X": 1,
        "Y": 5,
        "Z": 9
    },
    "C": {
        "X": 7,
        "Y": 2,
        "Z": 6
    }
}

scores_part_2 = {
    "A": {
        "X": 3,
        "Y": 4,
        "Z": 8
    },
    "B": {
        "X": 1,
        "Y": 5,
        "Z": 9
    },
    "C": {
        "X": 2,
        "Y": 6,
        "Z": 7
    }
}

total_score_part_1 = 0
total_score_part_2 = 0
with open('adventofcode2022/day_02_star_01/input_rps.txt') as inputfile:
    for line in inputfile:
        strings = line.strip().split()
        total_score_part_1 += scores_part_1[strings[0]][strings[1]]
        total_score_part_2 += scores_part_2[strings[0]][strings[1]]


print(total_score_part_1, total_score_part_2)