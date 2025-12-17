import re
from functools import cache
from pathlib import Path


def read_input(file_path: str | Path = "input.txt") -> list[int]:
    """Parse and validate instructions from the input file."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    content = path.read_text()
    if not content:
        raise ValueError(f"Input file is empty: {path}")

    lines = content.splitlines()

    if not re.match(r"^[\.S]+$", lines[0]):
        raise ValueError(
            f"Unexpected input format in {path}. Expected first line to contain only . and S"
        )

    if not all([re.match(r"^[\.\^]+$", line) for line in lines[1:]]):
        raise ValueError(
            f"Unexpected input format in {path}. Expected subsequent lines to contain only . and ^"
        )

    return lines


class Manifold:
    """Representation of a Tachyon Manifold"""

    def __init__(self, lines: list[str]) -> None:
        self.lines = lines
        self.start = lines[0].index("S")

    def count_splits(self) -> int:
        beams = {self.start}
        splits = 0
        for line in self.lines[1:]:
            events = set([x for x in range(len(line)) if line[x] != "." and x in beams])
            splits += len(events)
            new_beams = set([x + d for x in events for d in (-1, 1)])
            beams = beams.difference(events)
            beams = beams.union(new_beams)
        return splits

    @cache
    def count_quantum_splits(self, row: int = 0, col: int = None) -> int:
        if col is None:
            col = self.start
        if row == len(self.lines) - 1:
            return 1
        else:
            if self.lines[row + 1][col] == "^":
                return self.count_quantum_splits(row + 1, col - 1) + self.count_quantum_splits(
                    row + 1, col + 1
                )
            else:
                return self.count_quantum_splits(row + 1, col)


def main() -> None:
    lines = read_input("./solutions/2025/day-07/input.txt")
    manifold = Manifold(lines)
    part1 = manifold.count_splits()

    print(f"Part 1: {part1}")

    part2 = manifold.count_quantum_splits()
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
