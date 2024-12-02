#!/usr/bin/env python

from pathlib import Path


def split_into_columns(data: str) -> tuple[list[int], list[int]]:
    left = []
    right = []
    for line in data.splitlines():
        left_value, right_value = [int(value) for value in line.split(" ", 1)]
        left.append(left_value)
        right.append(right_value)

    return left, right

def calculate_total(column_one: list[int], column_two: list[int]) -> None:

    # Sort values
    column_one = sorted(column_one)
    column_two = sorted(column_two)

    # Calculate total
    total = 0
    for id, value in enumerate(column_one):
        total += abs(value - column_two[id])

    print(f"Total is {total:,}")

def similarity_score(column_one: list[int], column_two: list[int]) -> None:
    total = 0
    for value in column_one:
        count = column_two.count(value)
        total += value * count

    print(f"Similarity score is {total:,}")

def main():
    # Read the data and split into columns
    input = Path("input.txt")

    text = input.read_text()
    left, right = split_into_columns(text)
    calculate_total(left, right)
    similarity_score(left, right)


if __name__ == "__main__":
    main()
