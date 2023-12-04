from os import environ
from re import findall
from typing import Dict, List

numbers: Dict[str, str] = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_solution_part1(input_list: List[str]) -> int:
    total: int = 0
    first: str
    last: str
    for line in input_list:
        first = findall(r"(\d)", line)[0]
        last = findall(r"(\d)\D*?$", line)[0]
        total += int(first + last)
    return total


def get_solution_part2(input_list: List[str]) -> int:
    total: int = 0
    numre: str = r"(?=(\d|" + r"|".join(numbers.keys()) + r"))"
    first: str
    last: str
    for line in input_list:
        parsed: List[str] = findall(numre, line)
        if parsed[0] in numbers:
            first = numbers[parsed[0]]
        else:
            first = parsed[0]
        if parsed[-1] in numbers:
            last = numbers[parsed[-1]]
        else:
            last = parsed[-1]
        total += int(first + last)
    return total


if __name__ == "__main__":
    with open("input.txt", encoding="UTF-8") as f:
        file_input: List[str] = f.readlines()

    part: str | None = environ.get("part")

    if part == "part2":
        print(get_solution_part2(file_input))
    else:
        print(get_solution_part1(file_input))
