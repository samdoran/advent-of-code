#!/usr/bin/env python

from pathlib import Path


def is_safe(levels: list[int]) -> bool:
    deltas = []
    for id, level in enumerate(levels):
        if id == 0:
            continue

        delta = levels[id - 1] - level
        deltas.append(delta)

    all_increasing = all(value < 0 for value in deltas)
    all_decreasing = all(value > 0 for value in deltas)

    if not (all_increasing or all_decreasing):
        return False

    # Delta of at least 1 and at most 3
    if not all(0 < abs(i) < 4 for i in deltas):
        return False

    return True


def main():
    data = Path("input.txt").read_text()
    results = []
    for report in data.splitlines():
        levels = [int(level) for level in report.split(" ")]
        results.append(is_safe(levels))

    print(results.count(True))




if __name__ == "__main__":
    main()
