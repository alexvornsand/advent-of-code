import re
from pathlib import Path


def read_input(file_path: str | Path = "input.txt") -> list[int]:
    """Parse and validate instructions from the input file."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    content = path.read_text()
    if not content:
        raise ValueError(f"Input file is empty: {path}")

    blocks = content.strip().split("\n\n")

    raw_shapes = blocks[:-1]
    raw_regions = blocks[-1]

    if not all(re.match(r"^\d+:\n([\.#]{3}+\n?){3}$", shape) for shape in raw_shapes):
        raise ValueError(
            f"Unexpected input format in {path}. Expected each shape to be an index followed by a 3x3 grid of . and #."
        )

    if not all(re.match(r"^\d+x\d+:\s(\d+\s?)+$", region) for region in raw_regions.splitlines()):
        raise ValueError(
            f"Unexpected input format in {path}. "
            "Expected each region to be an size declaration followed by a list of shape counts."
        )

    def parse_shape(block: str) -> tuple[int | dict[str, dict[str, int] | dict[tuple[int]], bool]]:
        lines = [line for line in block.strip().split("\n") if line.strip()]
        header = lines[0].rstrip(":")
        number = int(header)
        grid = lines[1:]
        shape = {}
        count = 0

        for y, row in enumerate(grid):
            for x, char in enumerate(row):
                is_hash = char == "#"
                shape[(x, y)] = is_hash
                if is_hash:
                    count += 1
        return number, {"count": count, "shape": shape}

    def parse_region(region: str) -> dict[str, int | list[int]]:
        raw_size, raw_counts = region.strip().split(":")
        size = [int(x) for x in raw_size.strip().split("x")]
        counts = [int(x) for x in raw_counts.strip().split(" ")]
        return {"shape": {k: v for k, v in zip(["x", "y"], size)}, "counts": counts}

    shapes = dict(parse_shape(block) for block in raw_shapes)
    regions = [parse_region(region) for region in raw_regions.splitlines()]

    return shapes, regions


def main() -> None:
    shapes, regions = read_input("./solutions/2025/day-12/input.txt")

    part1 = sum(
        [
            region["shape"]["x"] * region["shape"]["y"]
            > sum([shapes[i]["count"] * count for i, count in enumerate(region["counts"])])
            for region in regions
        ]
    )
    print(f"Part 1: {part1}")


if __name__ == "__main__":
    main()
