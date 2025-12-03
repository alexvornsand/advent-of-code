# advent of code 2025
# day 2

from pathlib import Path
import re

class IDRange:
    """Represents a range of valid IDs to be analyzed"""
    def __init__(
            self,
            range_start: int,
            range_end: int
    ) -> None:
        self.range_start = range_start
        self.range_end = range_end

    def countTwinIDs(
            self,
    ) -> int:
        """Count the number of possible IDs within the range that match the repeating pattern"""
        return sum([candidate_id for candidate_id in range(self.range_start, self.range_end + 1) if bool(re.match(r"^(.*)\1$", str(candidate_id)))])

    def countMultipleIDs(
            self,
    ) -> int:
        """Count the number of possible IDs within the range that match the repeating pattern"""
        return sum([candidate_id for candidate_id in range(self.range_start, self.range_end + 1) if any([bool(re.match(r"^(.*)" + (r"\1" * (n - 1)) + r"$", str(candidate_id))) for n in range(2, len(str(candidate_id)) + 1)])])

def read_input(file_path: str | Path = "input.txt") -> list[int]:
    """Parse and validate instructions from the input file."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    content = path.read_text().strip()
    if not content:
        raise ValueError(f"Input file is empty: {path}")

    id_ranges = content.split(',')

    if not all(re.match(r"\d+\-\d+", id_range) for id_range in id_ranges):
        raise ValueError(
            f"Unexpected input format in {path}. "
            "Expected each range to contain exactly #-#."
        )

    return [[int(x) for x in re.findall(r"\d+", id_range)] for id_range in id_ranges]


def main() -> None:
    id_range_value_pairs = read_input(
        "./solutions/2025/day-01/input.txt"
    )
    id_ranges = [IDRange(*id_range_value_pair) for id_range_value_pair in id_range_value_pairs]
    part1 = sum([id_range.countTwinIDs() for id_range in id_ranges])

    print(f"Part 1: {part1}")

    part2 = sum([id_range.countMultipleIDs() for id_range in id_ranges])
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
