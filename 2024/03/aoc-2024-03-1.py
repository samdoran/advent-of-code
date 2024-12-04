#!/usr/bin/env python

import re
from pathlib import Path


def main():
    data = Path("input.txt").read_text()
    regexp = re.compile(r'mul\((\d+),(\d+)\)')
    matches = regexp.findall(data)
    print(sum(int(a) * int(b) for a, b in matches))

if __name__ == "__main__":
    main()
