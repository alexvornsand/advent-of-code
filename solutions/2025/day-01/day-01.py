# advent of code 2025
# day 1

from pathlib import Path
from typing import TypeAlias
import re

class Safe: 
    """Represents a safe evaluating instructions"""

    def __init__(
            self,
            instructions: list[int],
            default_position: int = 50
    ) -> None:
        self.instructions = instructions
        self.default_position = default_position
        self.position = default_position
        self.zero_lands: int = 0
        self.zero_crosses: int = 0

    def _evaluate_instruction(
            self,
            instruction: int
    ) -> None:
        """Process a single instruction and log if it crossed 0 or landed on 0"""
        sign = instruction / abs(instruction)
        laps = (sign * instruction) // 100
        net_change = instruction - (sign * laps * 100)
        turnover = 1 if self.position != 0 and (self.position + net_change >= 100 or self.position + net_change <= 0) else 0
        self.position = (self.position + net_change) % 100
        if self.position == 0:
            self.zero_lands += 1
        self.zero_crosses = int(self.zero_crosses + turnover + laps)

    def evaluate_instructions(
            self
    ) -> None:
        """Process all instructions sequentially"""
        for time, instruction in enumerate(self.instructions):
            self._evaluate_instruction(instruction)

    def count_zeroes(
        self
    ) -> int:
        """Surface both critical values"""
        return self.zero_lands, self.zero_crosses

def read_input(file_path: str | Path = "input.txt") -> list[int]:
    """Parse and validate instructions from the input file."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    content = path.read_text().strip()
    if not content:
        raise ValueError(f"Input file is empty: {path}")

    instructions = content.splitlines()

    if not all(re.match(r"[RL]\d+", instruction) for instruction in instructions):
        raise ValueError(
            f"Unexpected input format in {path}. "
            "Expected each line to contain exactly R# or L#."
        )

    return [int(instruction[1:]) if instruction[0] == 'R' else -int(instruction[1:]) for instruction in instructions]


def main() -> None:
    instructions = read_input(
        "./solutions/2025/day-01/input.txt"
    )
    safe = Safe(instructions)
    safe.evaluate_instructions()
    part1 = safe.count_zeroes()[0]

    print(f"Part 1: {part1}")

    part2 = safe.count_zeroes()[1]
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
