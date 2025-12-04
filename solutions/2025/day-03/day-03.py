from pathlib import Path
import re

def read_input(file_path: str | Path = "input.txt") -> list[int]:
    """Parse and validate instructions from the input file."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    content = path.read_text().strip()
    if not content:
        raise ValueError(f"Input file is empty: {path}")

    banks = content.splitlines()

    if not all(re.match(r"^\d+$", bank) for bank in banks):
        raise ValueError(
            f"Unexpected input format in {path}. "
            "Expected each range to contain exactly ^\\d+$."
        )

    return [[int(x) for x in bank] for bank in banks]

class BatteryBank:
    """Represents an array of batteries in sequence with their joltages"""
    def __init__(
            self,
            batteries: list[int]
    ) -> None:
        self.batteries = batteries

    def findMaximumBatteryJoltage(
            self,
            batteries: list[int] = None,
            digits: int = 2
    ) -> int:
        """Find the next largest digit for a number of length n"""
        if batteries is None:
            batteries = self.batteries
        digits -= 1
        if digits == 0:
            return max(batteries)
        else:
            next_digit = max(batteries[:-digits])
            batteries = batteries[batteries.index(next_digit) + 1:]
            return int(str(next_digit) + str(self.findMaximumBatteryJoltage(batteries=batteries, digits=digits)))
        
def main() -> None:
    banks = read_input(
        "./solutions/2025/day-03/input.txt"
    )
    battery_banks = [BatteryBank(bank) for bank in banks]
    part1 = sum(battery_bank.findMaximumBatteryJoltage() for battery_bank in battery_banks)

    print(f"Part 1: {part1}")

    part2 = sum(battery_bank.findMaximumBatteryJoltage(digits=12) for battery_bank in battery_banks)
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    main()