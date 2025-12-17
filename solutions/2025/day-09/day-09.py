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

    tiles = content.splitlines()

    if not all(re.match(r"^\d+,\d+$", tile) for tile in tiles):
        raise ValueError(
            f"Unexpected input format in {path}. Expected each line to contain exactly #,#"
        )

    return [tuple(int(coord) for coord in tile.split(",")) for tile in tiles]


class TileFloor:
    """A grid of floor tiles"""

    def __init__(self, tiles: list[int]) -> None:
        self.tiles = tiles
        self.tile_pairs = [(a, b) for a in tiles for b in tiles if a > b]
        self.edges = [
            sorted(tuple([tiles[i], tiles[(i + 1) % len(tiles)]])) for i in range(len(tiles))
        ]
        self.areas = {}

    def get_maximum_tile_area(self, constrained: bool = False, log: str = "None") -> int:
        """Get the largest rectangular area between red tiles"""
        return max(
            self._get_tile_area(*tile_pair, constrained=constrained, log=log)
            for tile_pair in self.tile_pairs
        )

    def _get_tile_area(
        self, a: tuple[int], b: tuple[int], constrained: bool = False, log: str = "None"
    ) -> int:
        x1, y1 = a
        x2, y2 = b
        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        if constrained:
            corners = [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]
            all_interior = all(self._check_interiority(corner) for corner in corners)
            no_crossings = all(
                self._check_edge_collisions(corners[i], corners[(i + 1) % 4]) for i in range(4)
            )
            if all_interior and no_crossings:
                self.areas[(a, b)] = area
            else:
                self.areas[(a, b)] = -1
            if log != "None":
                print(f"{(a, b)} (constrained: {constrained}): {area}")
                if log == "Print":
                    self._graph((a, b))
        else:
            self.areas[(a, b)] = area
            if log != "None":
                print(f"{(a, b)} (constrained: {constrained}): {area}")
                if log == "Print":
                    self._graph((a, b))
        return self.areas[(a, b)]

    def _graph(self, points: list[tuple[int]] = []) -> None:
        """Graph the floor tiles, optionally highlighting a set of points"""
        if self.tiles[0][0] > 20:
            print("Can't print large graphs")
        else:
            if not hasattr(self, "base_grid"):
                self._build_grid()
            print(
                "\n".join(
                    [
                        "".join(
                            [
                                self.base_grid[r][c] if (c, r) not in points else "O"
                                for c in range(len(self.base_grid[r]))
                            ]
                        )
                        for r in range(len(self.base_grid))
                    ]
                )
            )

    def _build_grid(self) -> None:
        """Build base graph content"""
        graph_dict = {}
        x_max = max([tile[0] for tile in self.tiles]) + 1
        y_max = max([tile[1] for tile in self.tiles]) + 1
        for x in range(x_max):
            for y in range(y_max):
                graph_dict[(x, y)] = "."
        for [(x1, y1), (x2, y2)] in self.edges:
            c_min = min([x1, x2])
            c_max = max([x1, x2]) + 1
            r_min = min([y1, y2])
            r_max = max([y1, y2]) + 1
            for r in range(r_min, r_max):
                for c in range(c_min, c_max):
                    graph_dict[(c, r)] = "X"
        for tile in self.tiles:
            graph_dict[tile] = "#"
        self.base_grid = [[graph_dict[(x, y)] for x in range(x_max)] for y in range(y_max)]

    def _check_edge_collisions(self, a: list[int], b: list[int]) -> int:
        """Check each box edge for collisions and return True if free of collisions and False if collisions"""
        (x1, y1), (x2, y2) = sorted([a, b])
        if x1 == x2:
            crosses_h_edge = not any(
                y1 < ly1 < y2 and lx1 < x1 < lx2 for ((lx1, ly1), (lx2, _)) in self.edges
            )
            return crosses_h_edge
        else:
            crosses_v_edge = not any(
                x1 < lx1 < x2 and ly1 < y1 < ly2 for ((lx1, ly1), (_, ly2)) in self.edges
            )
            return crosses_v_edge

    def _check_interiority(self, point: tuple[int]) -> bool:
        """Return True if point is inside or on the boundary of a rectilinear polygon."""
        x, y = point

        n = len(self.tiles)
        if n < 3:
            return False

        if self.tiles[0] != self.tiles[-1]:
            poly = list(self.tiles) + [self.tiles[0]]
        else:
            poly = list(self.tiles)

        for (x1, y1), (x2, y2) in zip(poly, poly[1:]):
            if y1 == y2 == y and min(x1, x2) <= x <= max(x1, x2):
                return True
            if x1 == x2 == x and min(y1, y2) <= y <= max(y1, y2):
                return True

        crossings = 0

        for (x1, y1), (x2, y2) in zip(poly, poly[1:]):
            if y1 == y2:
                continue

            if not (min(y1, y2) <= y < max(y1, y2)):
                continue

            x_intersect = x1 + (x2 - x1) * (y - y1) / (y2 - y1)

            if x_intersect > x:
                crossings += 1

        return (crossings % 2) == 1


def main() -> None:
    tiles = read_input("./solutions/2025/day-09/input.txt")

    tile_floor = TileFloor(tiles)
    part1 = tile_floor.get_maximum_tile_area()

    print(f"Part 1: {part1}")

    part2 = tile_floor.get_maximum_tile_area(constrained=True)
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
