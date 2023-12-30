import re
import numpy as np


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


def day3(input):
    parts_list = []
    star_part_dict = {}
    star_parts_list = []

    with open(input) as file:
        lines = [line.strip() for line in file]

    # deal with numbers ending line not getting recognised
    lines = [x + "." for x in lines]

    for i in range(len(lines)):
        line = lines[i]
        # print("\nLine number " + str(i) + ": " + line)
        count = 0
        for j in range(len(line)):
            if line[j].isdigit():
                count += 1
                # print("j =", j)
                # print("count = ", count)
            else:
                spec_char = []
                if line[j - count : j] != "":
                    # line above spec chars
                    above_chars = ""
                    if i - 1 >= 0:
                        if j - count - 1 >= 0:
                            # diagonal up left
                            above_chars = above_chars + lines[i - 1][j - count - 1]
                        else:
                            above_chars = above_chars + "."
                        # directly above
                        above_chars = above_chars + lines[i - 1][j - count : j]
                        if j <= len(line):
                            # diagonal up right
                            above_chars = above_chars + lines[i - 1][j]
                        else:
                            above_chars = above_chars + "."
                    else:
                        above_chars = "." * (count + 2)

                    spec_char.append(above_chars)

                    # same line spec chars
                    line_chars = ""
                    if j - count - 1 >= 0:
                        # before
                        line_chars = line_chars + line[j - count - 1]
                    else:
                        line_chars = line_chars + "."
                    line_chars = line_chars + ("." * count)
                    if j <= len(line):
                        # after
                        line_chars = line_chars + line[j]
                    else:
                        line_chars = line_chars + "."

                    spec_char.append(line_chars)

                    # line below spec chars
                    below_chars = ""
                    if i + 1 < len(lines):
                        if j - count - 1 >= 0:
                            # diagonal down left
                            below_chars = below_chars + lines[i + 1][j - count - 1]
                        else:
                            below_chars = below_chars + "."
                        # directly below
                        below_chars = below_chars + lines[i + 1][j - count : j]
                        if j <= len(line):
                            # diagonal down right
                            below_chars = below_chars + lines[i + 1][j]
                        else:
                            below_chars = below_chars + "."
                    else:
                        below_chars = "." * (count + 2)

                    spec_char.append(below_chars)

                    ### PART 1
                    # remove . from spec_char
                    spec_char_concat = " ".join(spec_char).replace(".", "").split()
                    if len(spec_char_concat) > 0:
                        parts_list.append(int(line[j - count : j]))

                    ### PART 2
                    star_char = []

                    star_char = np.argwhere(
                        np.array([list(x) for x in spec_char]) == "*"
                    )

                    if len(star_char) > 0:
                        for x in star_char:
                            x[0] = x[0] + (i - 1)
                            x[1] = x[1] + (j - count - 1)
                            if str(x) in star_part_dict:
                                star_part_dict[str(x)].append(int(line[j - count : j]))
                            else:
                                star_part_dict[str(x)] = [int(line[j - count : j])]

                count = 0

    for key in star_part_dict:
        if len(star_part_dict[key]) == 2:
            star_parts_list.append(star_part_dict[key][0] * star_part_dict[key][1])

    day3_1_result = sum(parts_list)
    print("\n  Day 3 - Task 1")
    print("  Answer: " + str(day3_1_result))

    day3_2_result = sum(star_parts_list)
    print("\n  Day 3 - Task 2")
    print("  Answer: " + str(day3_2_result))


def day4(input):
    points = []
    num_of_cards = 0
    card_ns = []

    with open(input) as file:
        cards = [line.strip() for line in file]

    cards = [card.split()[2:] for card in cards]

    for card in cards:
        winning_nums = card[: card.index("|")]
        nums_have = card[card.index("|") + 1 :]
        match_nums = sum(nums in nums_have for nums in winning_nums)
        # print("match_nums:", match_nums)

        # Part 1
        if match_nums > 0:
            points.append(2 ** (match_nums - 1))
        else:
            points.append(0)

        # Part 2
        num_of_cards = num_of_cards + match_nums + 1
        curr_card = cards.index(card) + 1
        card_ns.append(curr_card)
        num_instances = card_ns.count(curr_card)
        # print("current card game line:", curr_card)
        # print("number of instances of", curr_card, ":", num_instances)
        for i in range(match_nums):
            # print(
            #     "Adding card to deck:",
            #     curr_card + i + 1,
            #     "x",
            #     num_instances,
            #     "number of times",
            # )
            for j in range(num_instances):
                card_ns.append(cards.index(card) + i + 2)
        # print(card_ns)
        # print()

    day4_1_result = sum(points)
    print("\n  Day 4 - Task 1")
    print("  Answer: " + str(day4_1_result))

    day4_2_result = len(card_ns)
    print("\n  Day 4 - Task 2")
    print("  Answer: " + str(day4_2_result))


def day5_1(input):
    locations = []

    with open(input) as file:
        mappings = [line.strip() for line in file]
    # print("    File opened.")

    seeds = mappings[0].split()[1:]
    mappings = [i for i in mappings[2:] if i != ""]
    mappings.append("end of map")
    map_titles = [s for s in mappings if "map" in s]

    # print("    Sorting data...")

    for seed in seeds:
        # print("      Seed:", seed)
        seed = int(seed)
        value = seed

        for t in range(len(map_titles) - 1):
            index = mappings.index(map_titles[t])
            end_of_section = mappings.index(map_titles[t + 1])
            if end_of_section > len(mappings):
                end_of_section = len(mappings)

            map_name = mappings[index].split()[0].split("-")
            del map_name[1]
            map_name_data = [
                item.split() for item in mappings[index + 1 : end_of_section]
            ]
            # print("        Mapping:", str(map_name))

            # print(str(map_name), map_name_data)
            temp_value = value
            for data in map_name_data:
                source_start = int(data[1])
                destination_start = int(data[0])
                range_length = int(data[2])
                source_end = source_start + range_length
                # print(source_end, "=", source_start, "+", range_length)
                if temp_value >= source_start and temp_value < source_end:
                    # print(temp_value, "<", source_end)
                    value = destination_start + (value - source_start)
                    # print(data)
            # print(map_name[0], temp_value, map_name[1], value)

            if map_name[1] == "location":
                locations.append(value)

        # print(locations, "\n")

    day5_result = min(locations)
    print("\n  Day 5 - Task 1")
    print("  Answer: " + str(day5_result))


def day5_2(input, task2):
    if task2 == True:
        locations = [9999999999999]

        with open(input) as file:
            mappings = [line.strip() for line in file]
        # print("    File opened.")

        seeds = mappings[0].split()[1:]
        mappings = [i for i in mappings[2:] if i != ""]
        mappings.append("end of map")
        map_titles = [s for s in mappings if "map" in s]

        # print("    Sorting data...")
        # print(seeds)
        # print(seeds[::2])
        # print(seeds[1::2])
        seeds_start = seeds[::2]
        seeds_range = seeds[1::2]
        for i in range(len(seeds_start)):
            seeds2 = []
            print("Seed range:", seeds_start[i], seeds_range[i])
            for j in range(int(seeds_range[i])):
                # print(seeds_start[i], int(seeds_start[i]) + j)
                seeds2.append(int(seeds_start[i]) + j)

            for seed in seeds2:
                # print("      Seed:", seed)
                seed = int(seed)
                value = seed

                for t in range(len(map_titles) - 1):
                    index = mappings.index(map_titles[t])
                    end_of_section = mappings.index(map_titles[t + 1])
                    if end_of_section > len(mappings):
                        end_of_section = len(mappings)

                    map_name = mappings[index].split()[0].split("-")
                    del map_name[1]
                    map_name_data = [
                        item.split() for item in mappings[index + 1 : end_of_section]
                    ]
                    # print("        Mapping:", str(map_name))

                    # print(str(map_name), map_name_data)
                    temp_value = value
                    for data in map_name_data:
                        source_start = int(data[1])
                        destination_start = int(data[0])
                        range_length = int(data[2])
                        source_end = source_start + range_length
                        # print(source_end, "=", source_start, "+", range_length)
                        if temp_value >= source_start and temp_value < source_end:
                            # print(temp_value, "<", source_end)
                            value = destination_start + (value - source_start)
                            # print(data)
                    # print(map_name[0], temp_value, map_name[1], value)

                    if map_name[1] == "location":
                        if value < min(locations):
                            locations.append(value)
                            print("Location", value)

            # print(locations, "\n")

        day5_result = min(locations)
    else:
        day5_result = 15880236
    print("\n  Day 5 - Task 2")
    # Seed range: 3151642679 224376393
    # Location 15880236
    print("  Answer: " + str(day5_result))


def main():
    print("\n~~~ Advent Of Code 2023 ~~~\n")
    # day1_1("inputs/day1.txt")
    # day1_2("inputs/day1.txt")
    # day2("inputs/day2.txt")
    # day3("inputs/day3.txt")
    # day4("inputs/day4.txt")
    # day5_1("inputs/day5.txt")
    day5_2("inputs/day5.txt", False)


main()
