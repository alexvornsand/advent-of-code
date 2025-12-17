import math
import re
from collections import deque
from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx


def read_input(file_path: str | Path = "input.txt") -> list[int]:
    """Parse and validate instructions from the input file."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    content = path.read_text()
    if not content:
        raise ValueError(f"Input file is empty: {path}")

    boxes = content.splitlines()

    if not all(re.match(r"^\d+,\d+,\d+$", box) for box in boxes):
        raise ValueError(
            f"Unexpected input format in {path}. Expected each line to contain exactly #,#,#"
        )

    return [tuple(int(coord) for coord in box.split(",")) for box in boxes]


class BoxNetwork:
    """Network of independent and interconnected junction boxes"""

    def __init__(self, boxes: tuple[int]) -> None:
        self.boxes = boxes
        self.pair_queue = deque(
            sorted(
                [(box_a, box_b) for box_a in self.boxes for box_b in self.boxes if box_a > box_b],
                key=lambda x: math.dist(x[0], x[1]),
            )
        )
        self.graph = nx.Graph()
        self.graph.add_nodes_from(self.boxes)

    def build_network(self, n=1000) -> int:
        """Build the network by connecting n disconnected boxes"""
        self._reset_graph()
        for _ in range(n):
            self._link_boxes()
        return self._quantify_circuits()

    def build_complete_network(self) -> int:
        """Build the network until you have one large circuit"""
        self._reset_graph()
        while True:
            x_dist = self._link_boxes()
            if len(list(nx.connected_components(self.graph))) == 1:
                return x_dist

    def _link_boxes(self) -> int:
        """Connect closest boxes that aren't already in the same network"""
        node_a, node_b = self.pair_queue.popleft()
        if node_a not in self.graph.neighbors(node_b):
            self.graph.add_edge(node_a, node_b)
            return node_a[0] * node_b[0]

    def _quantify_circuits(self) -> int:
        """Multiply the sizes of the three largest circuits"""
        return math.prod(
            sorted(
                [len(self.graph.subgraph(c).copy()) for c in nx.connected_components(self.graph)],
                reverse=True,
            )[:3]
        )

    def _print_graph(self) -> None:
        """Print the graph"""
        nx.draw(
            self.graph,
            with_labels=True,
            node_color="skyblue",
            node_size=50,
            font_size=10,
            font_weight="bold",
        )
        plt.show()

    def _reset_graph(self) -> None:
        """Reset graph to default status"""
        self.pair_queue = deque(
            sorted(
                [(box_a, box_b) for box_a in self.boxes for box_b in self.boxes if box_a > box_b],
                key=lambda x: math.dist(x[0], x[1]),
            )
        )
        self.graph = nx.Graph()
        self.graph.add_nodes_from(self.boxes)


def main() -> None:
    boxes = read_input("./solutions/2025/day-08/input.txt")
    box_network = BoxNetwork(boxes)
    part1 = box_network.build_network()

    print(f"Part 1: {part1}")

    part2 = box_network.build_complete_network()
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
