#!/usr/bin/env python

import shutil
import sys

from pathlib import Path

DIRECTIONS = (
    (0, -1, "←"),
    (1, -1, "↙︎"),
    (1, 0, "↓"),
    (1, 1, "↘︎"),
    (0, 1, "→"),
    (-1, 1, "↗︎"),
    (-1, 0, "↑"),
    (-1, -1, "↖︎"),
)

def check_grid(grid: list[str], word: str, row: int, column: int) -> int:
    if grid[row][column] != word[0]:
        return False

    grid_width = len(grid[0])
    grid_height = len(grid)

    # Check around the current letter for all occurrences of the word
    found = 0
    for x, y, flair in DIRECTIONS:
        current_x = row + x
        current_y = column + y
        print(f"Found 'X' at {row, column}")

        for letter in word[1:]:
            print(f"Checking for {letter} at {current_x, current_y} {flair}")

            # Bounds check
            if current_x >= grid_width or current_x < 0 or current_y >= grid_height or current_y < 0:
                print("  ↳ Out of bounds")
                break

            # Not a match
            if (test_letter := grid[current_x][current_y]) != letter:
                print(f"  ↳ Nope: {test_letter}")
                break

            # Next direction
            current_x += x
            current_y += y
        else:
            # Word found
            print("🎄")
            found += 1

    return found

def main():
    data = Path("input.txt").read_text()
    matrix = [ line.upper() for line in data.splitlines() ]
    word = sys.argv[1].upper()

    count = 0
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            count += check_grid(matrix, word, row, column)

    # Don't want to blow up the window with emoji spam
    max_width = min(count, shutil.get_terminal_size().columns // 2)
    print("🎄" * max_width)
    print(f"Found {count} occurencense of {word.upper()}")
    print("🎄" * max_width)


if __name__ == "__main__":
    main()
