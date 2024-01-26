#!/usr/bin/env python3
import re
import sys
from itertools import product

NUMBER_RE = re.compile(r'\d+')
SYMBOL_RE = re.compile(r'\W')


class Schematic:
    def __init__(self, lines: list[str]) -> None:
        self._lines = list(lines)

    def calculate_sum(self):
        def _is_adjecent(start, stop, line_number):
            print(f"Coords: {(start, stop)} at line: {line_number}")
            xs = filter(lambda l: l >= 0 and l < len(self._lines),
                range(line_number - 1, line_number + 2, 2))
            ys = filter(lambda n: n >= 0 and n < len(self._lines[line_number]),
                range(start - 1, stop + 1))

            return any(self._lines[x][y] != '.' and not self._lines[x][y].isalnum()
                       for x, y in product(xs, ys))

        return sum(int(m.group())
                   for line_number, line in enumerate(self._lines)
                   for m in NUMBER_RE.finditer(line)
                   if _is_adjecent(*m.span(), line_number))
                


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as fp:
        print(Schematic(fp.readlines()).calculate_sum())
