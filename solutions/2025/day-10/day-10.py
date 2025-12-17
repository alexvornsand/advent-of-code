import re
from pathlib import Path

import pulp as pl


def read_input(file_path: str | Path = "input.txt") -> list[int]:
    """Parse and validate instructions from the input file."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    content = path.read_text()
    if not content:
        raise ValueError(f"Input file is empty: {path}")

    lines = content.splitlines()

    if not all(
        re.match(r"^\[[\.#]+\]\s\(\d+(,\d+)*\)(\s\(\d+(,\d+)*\))*\s\{\d+(,\d+)*\}$", line)
        for line in lines
    ):
        raise ValueError(
            f"Unexpected input format in {path}. Expected each line to contain exactly\n"
            "\t1. a pair of brackets containing only . and # like [.##.]\n"
            "\t2. one or more sets of parentheses containing comma-separated integers like (3) (1,3)\n"
            "\t3. a pair of braces containing comma-separated integers like {3,5,4,7}"
        )

    def parse_line(line: str) -> list[list[int] | list[list[int]]]:
        pattern = re.compile(r"\[([.#]+)\]\s((?:\(\d+(?:,\d+)*\)\s*)+)\{(\d+(?:,\d+)*)\}")
        m = pattern.match(line)
        lights = [0 if char == "." else 1 for char in m.group(1)]
        buttons = [
            [int(char) for char in button.split(",")]
            for button in re.findall(r"\(([^)]+)\)", m.group(2))
        ]
        joltages = [int(char) for char in m.group(3).split(",")]
        return lights, buttons, joltages

    return [parse_line(line) for line in lines]


def solve_problem(lights, buttons, joltages, configuration="Lights") -> int:
    button_map = {
        i: [j for j in range(len(buttons)) if i in buttons[j]] for i in range(len(lights))
    }
    prob = pl.LpProblem("Machine", pl.LpMinimize)
    x = pl.LpVariable.dicts("x", range(len(lights)), lowBound=0, cat="Integer")
    if configuration == "Lights":
        b = pl.LpVariable.dicts("b", range(len(buttons)), lowBound=0, cat="Binary")
        y = pl.LpVariable.dicts("y", range(len(lights)), lowBound=0, cat=pl.LpInteger)
    else:
        b = pl.LpVariable.dicts("b", range(len(buttons)), lowBound=0, cat=pl.LpInteger)
    for i in range(len(lights)):
        prob += x[i] == pl.lpSum([b[j] for j in button_map[i]])
        if configuration == "Lights":
            prob += x[i] == (2 * y[i]) + lights[i]
        else:
            prob += x[i] == joltages[i]
    prob += pl.lpSum(b[i] for i in range(len(buttons)))
    prob.solve(pl.PULP_CBC_CMD(msg=False))
    return int(sum([b[i].varValue for i in range(len(buttons))]))


def main() -> None:
    manuals = read_input("./solutions/2025/day-10/input.txt")

    part1 = sum(solve_problem(*manual) for manual in manuals)
    print(f"Part 1: {part1}")

    part2 = sum(solve_problem(*manual, configuration="Joltages") for manual in manuals)
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
