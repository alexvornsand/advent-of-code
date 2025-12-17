import re
from functools import cache
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

    lines = content.splitlines()

    if not all(re.match(r"^\w+:\s\w+(\s\w+)*$", line) for line in lines):
        raise ValueError(
            f"Unexpected input format in {path}. Expected each line to contain 'www: xxx yyy zzz'"
        )

    def parse_line(line: str) -> tuple[str | list[str]]:
        pattern = re.compile(r"(\w+):\s(\w+(\s\w+)*)")
        m = pattern.match(line)
        key = m.group(1)
        values = [val for val in m.group(2).split(" ")]
        return tuple([key, values])

    return dict([parse_line(line) for line in lines])


class ServerNetwork:
    """DAG of interconnected serveres"""

    def __init__(self, network_map: dict[str, list[str]]) -> None:
        self.network_map = network_map

    @cache
    def find_exits(self, from_node: str = "you", to_node: str = "out") -> int:
        """Find the number of routes to 'out' from the current position"""
        if from_node == to_node:
            return 1
        if from_node not in self.network_map.keys():
            return 0
        neighbors = self.network_map[from_node]
        if len(neighbors) == 0:
            return 0
        else:
            return sum(
                self.find_exits(from_node=neighbor, to_node=to_node) for neighbor in neighbors
            )

    def _print_graph(self, special_nodes: list[str] = None) -> None:
        """Print the graph"""
        G = nx.DiGraph(self.network_map)
        pos = nx.kamada_kawai_layout(G)
        plt.figure(figsize=(10, 8))
        nx.draw_networkx_edges(
            G,
            pos,
            arrows=True,
            arrowsize=8,
            width=0.3,
            alpha=0.25,
            edge_color="black",
        )

        # Split nodes into “normal” and “special”
        if special_nodes is None:
            special_nodes = []
        special_nodes = set(special_nodes)
        normal_nodes = [n for n in G.nodes if n not in special_nodes]

        # --- Normal nodes: tiny, dark points, no labels ---
        nx.draw_networkx_nodes(
            G,
            pos,
            nodelist=normal_nodes,
            node_size=20,  # very small
            node_color="black",
            alpha=0.7,
        )

        # --- Special nodes: larger + labeled ---
        if special_nodes:
            nx.draw_networkx_nodes(
                G,
                pos,
                nodelist=list(special_nodes),
                node_size=120,
                node_color="tab:red",
                alpha=0.9,
            )
            labels = {n: str(n) for n in special_nodes}
            nx.draw_networkx_labels(
                G,
                pos,
                labels=labels,
                font_size=8,
                font_color="black",
            )

        plt.axis("off")
        plt.tight_layout()
        plt.show()


def main() -> None:
    network_map = read_input("./solutions/2025/day-11/input.txt")

    server_network = ServerNetwork(network_map)

    part1 = server_network.find_exits()
    print(f"Part 1: {part1}")

    part2 = (
        server_network.find_exits(from_node="svr", to_node="fft")
        * server_network.find_exits(from_node="fft", to_node="dac")
        * server_network.find_exits(from_node="dac")
    )
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
