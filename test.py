import re


def extract_numerical_words(input_string):
    word_to_number = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    # Create a regular expression pattern to match numerical words
    pattern = re.compile(
        r"\b(?:" + "|".join(word_to_number.keys()) + r")\b", re.IGNORECASE
    )

    # Find all matches in the input string
    matches = re.findall(pattern, input_string)
    print(matches)
    # Convert matches to numerical values
    numerical_values = [word_to_number[match.lower()] for match in matches]

    return numerical_values


# Example usage
input_string = "eightwothree"
result = extract_numerical_words(input_string)
print(f"The numerical words in the order they appear: {result}")
