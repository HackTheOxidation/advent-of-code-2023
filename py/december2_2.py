import re
import sys

from dataclasses import dataclass
from enum import Enum

GAME_RE = re.compile(r"Game (?P<gid>\d*): ")
DRAW_RE = re.compile(r"((?P<no>\d*) (?P<colour>(blue|red|green)))(,)*")


@dataclass(frozen=True)
class Draw:
    blue: int = 0
    red: int = 0 
    green: int = 0


class Game:
    def __init__(self, gid, *draws: list[Draw]):
        self._gid = int(gid)
        self._draws = list(draws)

    @staticmethod
    def from_string(string: str):
        kwargify = re.sub(DRAW_RE, r"\g<colour>=\g<no>,", string)
        constructed = re.sub(";", "), Draw(", kwargify)
        return eval(re.sub(GAME_RE, r"Game(\g<gid>, Draw(", constructed) + '))')

    def is_possible(self, bag: Draw) -> bool:
        for draw in self._draws:
            if bag.blue < draw.blue or bag.green < draw.green or bag.red < draw.red:
                return False

        return True

    def minimum_cubes(self) -> Draw:
        pass

    def __repr__(self):
        return f"<Game draws={self._draws.__repr__}>"


def read_file(filename):
    with open(filename, 'r') as fp:
        yield from fp.readlines()


if __name__ == '__main__':
    filename = sys.argv[1]
    games = (Game.from_string(line) for line in read_file(filename))
    bag = Draw(red=12, green=13, blue=14)
    gid_sum = sum(game._gid for game in games if game.is_possible(bag))
    print(gid_sum)

