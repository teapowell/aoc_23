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


def main():
    print("\n~~~ Advent Of Code 2023 ~~~\n")
    day1_1("/Users/tim.powell/Documents/vcs/aoc_23/inputs/day1.txt")
    day1_2("/Users/tim.powell/Documents/vcs/aoc_23/inputs/day1.txt")


main()
