from pathlib import Path
import re
from intervaltree import Interval, IntervalTree

def read_input(file_path: str | Path = "input.txt") -> list[int]:
    """Parse and validate instructions from the input file."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    content = path.read_text().strip()
    if not content:
        raise ValueError(f"Input file is empty: {path}")

    blocks = content.split('\n\n')

    if len(blocks) != 2:
        raise ValueError(
            f"Unexpected input format in {path}. "
            "Expected two blocks: ranges and values"
        )
    
    ranges_block, values_block = blocks
    ranges = ranges_block.splitlines()
    values = values_block.splitlines()

    if not all(re.match(r"^\d+\-\d+$", id_range) for id_range in ranges):
        raise ValueError(
            f"Unexpected input format in {path}. "
            "Expected each range to contain only #-#"
        )

    if not all(re.match(r"^\d+$", id) for id in values):
        raise ValueError(
            f"Unexpected input format in {path}. "
            "Expected each value to be only numbers"
        )

    return [tuple(int(val) for val in id_range.split('-')) for id_range in ranges], [int(val) for val in values]

class IngredientsDatabase:
    """Database of Ingredients"""
    def __init__(
            self,
            id_ranges,
            ids
    ) -> None:
        self.id_ranges = id_ranges
        self.ids = ids

    def countFreshIngredients(self) -> int:
        """Count ingredients whose id is in any valid id range"""
        return sum([any(id >= id_range[0] and id <= id_range[1] for id_range in self.id_ranges) for id in self.ids])

    def countTotalFreshValues(self) -> int:
        """Count number of all possible ids that are in any valid id range"""
        aggregate_ranges = IntervalTree([Interval(id_range[0], id_range[1] + 1) for id_range in self.id_ranges])
        aggregate_ranges.merge_overlaps()
        return sum([id_range[1] - id_range[0] for id_range in aggregate_ranges])
    
def main() -> None:
    id_ranges, ids = read_input(
        "./solutions/2025/day-05/input.txt"
    )
    ingredients_database = IngredientsDatabase(id_ranges, ids)
    part1 = ingredients_database.countFreshIngredients()

    print(f"Part 1: {part1}")

    part2 = ingredients_database.countTotalFreshValues()
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    main()