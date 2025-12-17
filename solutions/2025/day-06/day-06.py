import math
import re
from pathlib import Path

import numpy as np


def read_input(file_path: str | Path = "input.txt") -> list[int]:
    """Parse and validate instructions from the input file."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    content = path.read_text()
    if not content:
        raise ValueError(f"Input file is empty: {path}")

    lines = content.splitlines()

    if len(lines) < 3:
        raise ValueError(
            f"Unexpected input format in {path}. Expected at least three lines of data"
        )

    int_lines, ops = lines[:-1], lines[-1]

    if not all(re.match(r"^(\d+\s+)+\d+$", int_line.strip()) for int_line in int_lines):
        raise ValueError(
            f"Unexpected input format in {path}. "
            "Expected each integer line to contain only integers separated by spaces"
        )

    if not re.match(r"^([\+\*]\s+)+[\+\*]$", ops.strip()):
        raise ValueError(
            f"Unexpected input format in {path}. "
            "Expected the operator line to have only + and * separated by spaces"
        )

    if not all(len(int_line.split()) == len(int_lines[0].split()) for int_line in int_lines):
        raise ValueError(
            f"Unexpected input format in {path}. "
            "Expected each integer line to have the same number of integers"
        )

    if len(ops.split()) != len(int_lines[0].split()):
        raise ValueError(
            f"Unexpected input format in {path}. "
            "Expected operator line to have the same number of entries as the integer lines"
        )
    return int_lines, ops


class Worksheet:
    """Worksheet of math problems"""

    def __init__(self, int_lines: list[int], ops: list[str]) -> None:
        self.int_lines = int_lines
        self.ops = ops

    def get_checksum(self, transform: bool = False) -> int:
        """Calculate the sum of the solutions to the problems"""
        if transform is False:
            if not hasattr(self, "values"):
                self._solve_problems()
            return sum(self.values)
        else:
            reversed_lines = [[char for char in line[::-1]] for line in self.int_lines + [self.ops]]
            transposed = np.array(reversed_lines).transpose()
            joined_columns = [str.join("", column) for column in transposed]
            normalized = [re.sub(r"^\s+$", "-", col) for col in joined_columns]
            chunks = str.join("", normalized).split("-")
            return sum(
                [
                    eval(re.sub(r"\s+", chunk.strip()[-1], chunk.strip()[:-1].strip()))
                    for chunk in chunks
                ]
            )

    def _solve_problems(self) -> None:
        """Evaluate each math problem"""
        int_lines, ops = (
            [[int(val) for val in line.split()] for line in self.int_lines],
            [op for op in self.ops.split()],
        )
        problems = np.array(int_lines).transpose()
        self.values = [
            sum(problems[i]) if ops[i] == "+" else math.prod(problems[i]) for i in range(len(ops))
        ]


def main() -> None:
    int_lines, ops = read_input("./solutions/2025/day-06/input.txt")
    worksheet = Worksheet(int_lines, ops)
    part1 = worksheet.get_checksum()

    print(f"Part 1: {part1}")

    part2 = worksheet.get_checksum(transform=True)
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
