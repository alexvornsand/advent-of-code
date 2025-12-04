from pathlib import Path
import re
from collections import defaultdict

def read_input(file_path: str | Path = "input.txt") -> list[int]:
    """Parse and validate instructions from the input file."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    content = path.read_text().strip()
    if not content:
        raise ValueError(f"Input file is empty: {path}")

    rows = content.splitlines()

    if not all(re.match(r"^[\.@]*$", row) for row in rows):
        raise ValueError(
            f"Unexpected input format in {path}. "
            "Expected each range to contain only .@"
        )

    if not len(set(len(row) for row in rows)) == 1:
        raise ValueError(
            f"Unexpected input format in {path}. "
            "Expected all rows to be equal length"
        )

    return [[char for char in row] for row in rows]

class Grid:
    """Grid representing placement of rolls of paper"""
    def __init__(
            self,
            grid_array: list[list[str]]
    ) -> None:
        self.neighbors: dict[tuple[int], int] = {}
        self.grid = defaultdict(lambda: '.')
        for row in range(len(grid_array)):
            for col in range(len(grid_array[row])):
                self.grid[(col, row)] = grid_array[row][col]
        self.grid_rolls = list(self.grid.values()).count('@')

    def countAccessibleRolls(
            self,
            recursive: bool = False
        ) -> int:
        """Count the cells with rolls of paper and fewer than 4 neighboring rolls of paper"""
        recurse = False
        accessible = []
        for col, row in list(self.grid.keys()):
            neighbors = self._countNeighbors(col=col, row=row)
            if self.grid[(col, row)] == '@' and neighbors < 4:
                accessible.append((col, row))
                if recursive:
                    recurse = True
        for key in accessible:
            self.grid[key] = '.'
        if recurse is True:
            return self.countAccessibleRolls(recursive=recursive)
        else:
            return self.grid_rolls - list(self.grid.values()).count('@')

    def _countNeighbors(
            self,
            col: int,
            row: int
        ) -> int:
        """Count the neighbors for a cell"""
        neighbors = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
        self.neighbors[(col, row)] = sum([self.grid[(col + dc, row + dr)] == '@' for dc, dr in neighbors])
        return self.neighbors[(col, row)]
    
def main() -> None:
    grid_array = read_input(
        "./solutions/2025/day-04/input.txt"
    )
    grid = Grid(grid_array)
    part1 = grid.countAccessibleRolls()

    print(f"Part 1: {part1}")

    part2 = grid.countAccessibleRolls(recursive=True)
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    main()