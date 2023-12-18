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


def day3_1(input):
    parts_list = []

    with open(input) as file:
        lines = [line.strip() for line in file]

    for i in range(len(lines)):
        line = lines[i]
        # print("\nLine number " + str(i) + ": " + line)
        count = 0
        x = 0
        for j in range(len(line)):
            if line[j].isdigit():
                count += 1
            else:
                spec_char = []
                if line[j - count : j] != "":
                    # deal with low edge case
                    if j - count - 1 < 0:
                        low_j_calc = 0
                    else:
                        low_j_calc = j - count - 1
                    # deal with high edge case
                    if j + 1 > len(line):
                        high_j_calc = len(line)
                    else:
                        high_j_calc = j + 1

                    if i > 0:
                        # line above spec chars
                        spec_char.append(lines[i - 1][low_j_calc:high_j_calc])
                    if low_j_calc > 0:
                        # before num spec chars
                        spec_char.append(lines[i][low_j_calc])
                    if high_j_calc < len(line):
                        # after num spec chars
                        spec_char.append(lines[i][j])
                    if i + 1 < len(lines):
                        # line below spec chars
                        spec_char.append(lines[i + 1][low_j_calc:high_j_calc])

                    # remove numbers and . from spec_char
                    spec_char_concat = ("".join(spec_char)).translate(
                        {ord(i): None for i in "1234567890."}
                    )
                    if len(spec_char_concat) > 0:
                        parts_list.append(int(line[j - count : j]))

                    # print(
                    #     "Part: " + line[j - count : j] + " has spec_chars:",
                    #     spec_char,
                    #     "OR",
                    #     spec_char_concat,
                    # )

                count = 0
            x += 1
        # print("Parts:", parts_list)

    day3_1_result = sum(parts_list)
    print("\n  Day 2 - Task 2")
    print("  Answer: " + str(day3_1_result))


def main():
    print("\n~~~ Advent Of Code 2023 ~~~\n")
    # day1_1("inputs/day1.txt")
    # day1_2("inputs/day1.txt")
    # day2("inputs/day2.txt")
    day3_1("inputs/day3.txt")


main()
