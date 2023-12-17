import re


def day1_1(input):
    line_values = []
    with open(input) as file:
        lines = [line.strip() for line in file]
    for line in lines:
        line_nums_temp = list(line)
        line_nums = []
        for num in line_nums_temp:
            if num.isdigit():
                line_nums.append(num)
        line_values.append(int(line_nums[0] + line_nums[-1]))
    # print(line_values)

    day1_1_result = sum(line_values)
    print("\n  Day 1 - Task 1")
    print("  Answer: " + str(day1_1_result))


def day1_2(input):
    line_values = []

    with open(input) as file:
        lines = [line.strip() for line in file]
    for line in lines:
        # print(line)
        line = line.replace("zero", "z0o")
        line = line.replace("one", "o1e")
        line = line.replace("two", "t2o")
        line = line.replace("three", "t3e")
        line = line.replace("four", "f4r")
        line = line.replace("five", "f5e")
        line = line.replace("six", "s6x")
        line = line.replace("seven", "s7n")
        line = line.replace("eight", "e8t")
        line = line.replace("nine", "n9e")
        # print(line)
        line_nums_temp = list(line)
        line_nums = []
        for num in line_nums_temp:
            if num.isdigit():
                line_nums.append(num)
        line_values.append(int(line_nums[0] + line_nums[-1]))
        # print(line_values)

    day1_2_result = sum(line_values)
    print("\n  Day 1 - Task 2")
    print("  Answer: " + str(day1_2_result))


def day2(input):
    red_cubes = 12
    green_cubes = 13
    blue_cubes = 14
    poss_games = []
    power_games = []

    # open file
    with open(input) as file:
        lines = [line.strip() for line in file]

    for line in lines:
        # initiate game colour dict
        game_col_dict = {"red": [], "green": [], "blue": []}
        # split string
        spl_line = re.split(": |, |; | ", line)
        # get only colour info
        game_col = spl_line[2:]
        # get all values of cubes pulled
        for i in range(0, len(game_col), 2):
            game_col_dict[game_col[i + 1]].append(int(game_col[i]))
        # get max value of cubes pulled
        game_col_dict["red"] = max(game_col_dict["red"])
        game_col_dict["green"] = max(game_col_dict["green"])
        game_col_dict["blue"] = max(game_col_dict["blue"])
        # check if possible game
        if (
            game_col_dict["red"] <= red_cubes
            and game_col_dict["green"] <= green_cubes
            and game_col_dict["blue"] <= blue_cubes
        ):
            poss_games.append(int(spl_line[1]))
        # calculate power games
        power_games.append(
            game_col_dict["red"] * game_col_dict["green"] * game_col_dict["blue"]
        )

    day2_1_result = sum(poss_games)
    print("\n  Day 2 - Task 1")
    print("  Answer: " + str(day2_1_result))

    day2_2_result = sum(power_games)
    print("\n  Day 2 - Task 2")
    print("  Answer: " + str(day2_2_result))


def main():
    print("\n~~~ Advent Of Code 2023 ~~~\n")
    day1_1("/Users/tim.powell/Documents/vcs/aoc_23/inputs/day1.txt")
    day1_2("/Users/tim.powell/Documents/vcs/aoc_23/inputs/day1.txt")
    day2("/Users/tim.powell/Documents/vcs/aoc_23/inputs/day2.txt")


main()
