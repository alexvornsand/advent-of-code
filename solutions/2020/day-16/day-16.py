# advent of code 2020
# day 16

from datetime import datetime
from pathlib import Path
from typing import TypeAlias
import math


class Ticket:
    """Represents a ticket with values to be validated and mapped to field rules."""

    def __init__(
        self,
        field_rules: dict[str, list[list[int]]],
        values: list[int],
    ) -> None:
        self.field_rules = field_rules
        self.values = dict(enumerate(values))
        self.field_candidates: dict[int, set[str]] = {i: set() for i in self.values}
        self.value_candidates: dict[str, set[int]] = {
            name: set() for name in self.field_rules
        }
        self.fields: dict[str, int] = {}
        self.unmapped_fields = set(self.field_rules)
        self.unmapped_values = set(self.values)
        self.valid_ticket: bool | None = None
        self.invalid_values: list[int] = []

    def evaluate_values(
        self,
        exclusive: bool = True,
        log: bool = False,
        log_depth: int = 0,
    ) -> None:
        """Iterate over all values to progressively map them to fields."""
        for value_id in list(self.unmapped_values):
            if value_id in self.unmapped_values:
                self._log(
                    log_depth,
                    f"Evaluating value #{value_id} ({self.values[value_id]})",
                    log=log,
                )
                self._evaluate_value(
                    value_id, exclusive, log=log, log_depth=log_depth + 1
                )
            else:
                self._log(
                    log_depth,
                    f"Value #{value_id} ({self.values[value_id]}) already mapped",
                    log=log,
                )
        self.valid_ticket = len(self.invalid_values) == 0

    def __repr__(self) -> str:
        return f"Ticket(fields={self.fields}, valid={self.valid_ticket})"

    def _evaluate_value(
        self,
        value_id: int,
        exclusive: bool = True,
        visited: set[str] | None = None,
        log: bool = False,
        log_depth: int = 0,
    ) -> None:
        """Evaluate a single value against all field rules to identify candidate fields."""
        value = self.values[value_id]
        for field in self.unmapped_fields:
            self._log(
                log_depth,
                f"Comparing value #{value_id} ({value}) against field "
                f"'{field}' ({self.field_rules[field]})",
                log=log,
            )
            self._evaluate_value_against_rule(
                value_id, field, log=log, log_depth=log_depth + 1
            )
        if value_id in self.field_candidates:
            self._test_field_candidates_set(
                value_id,
                exclusive=exclusive,
                visited=visited,
                log=log,
                log_depth=log_depth + 1,
            )

    def _assign_field_value_pair(
        self,
        field: str,
        value_id: int,
        exclusive: bool = True,
        visited: set[str] | None = None,
        log: bool = False,
        log_depth: int = 0,
    ) -> None:
        """Assign a field to a value."""
        self._log(
            log_depth,
            f"Assigning value #{value_id} ({self.values[value_id]}) to field '{field}'",
            log=log,
        )
        visited = visited or set()
        self.unmapped_fields.discard(field)
        self.unmapped_values.discard(value_id)
        self.fields[field] = value_id
        self.value_candidates[field].discard(value_id)
        del self.field_candidates[value_id]

        if exclusive and self.value_candidates[field]:
            self._refine_field(field, visited, log=log, log_depth=log_depth + 1)

        del self.value_candidates[field]

    def _test_field_candidates_set(
        self,
        value_id: int,
        exclusive: bool = True,
        visited: set[str] | None = None,
        log: bool = False,
        log_depth: int = 0,
    ) -> None:
        """Test actionable cases in length of candidate sets."""
        if not self.field_candidates[value_id]:
            self._log(
                log_depth,
                f"Value #{value_id} ({self.values[value_id]}) has no candidate fields",
                log=log,
            )
            self.invalid_values.append(self.values[value_id])
            self.unmapped_values.discard(value_id)
            return

        if len(self.field_candidates[value_id]) == 1:
            assigned_field = next(iter(self.field_candidates[value_id]))
            self._log(
                log_depth,
                f"Value #{value_id} ({self.values[value_id]}) has only one candidate "
                f"field: {assigned_field}",
                log=log,
            )
            self._assign_field_value_pair(
                assigned_field,
                value_id,
                exclusive,
                visited=visited,
                log=log,
                log_depth=log_depth + 1,
            )

    def _evaluate_value_against_rule(
        self,
        value_id: int,
        field: str,
        log: bool = False,
        log_depth: int = 0,
    ) -> None:
        """Test a single value against a single rule."""
        value = self.values[value_id]
        match = any(lo <= value <= hi for lo, hi in self.field_rules[field])
        if match:
            self.field_candidates[value_id].add(field)
            self.value_candidates[field].add(value_id)
        self._log(
            log_depth,
            f"Value {'satisfies' if match else 'does not satisfy'} rule '{field}'",
            log=log,
        )

    def _refine_field(
        self,
        field: str,
        visited: set[str] | None = None,
        log: bool = False,
        log_depth: int = 0,
    ) -> None:
        """Refine candidate values for the given field by removing already mapped values."""
        visited = visited or set()
        if field in visited or not self.value_candidates[field]:
            return

        self._log(
            log_depth,
            f"Removing '{field}' as a candidate from values {self.value_candidates[field]}",
            log=log,
        )
        visited.add(field)

        for value_candidate in list(self.value_candidates[field]):
            self.field_candidates[value_candidate].discard(field)
            if value_candidate in self.field_candidates:
                self._test_field_candidates_set(
                    value_candidate,
                    exclusive=True,
                    visited=visited,
                    log=log,
                    log_depth=log_depth + 1,
                )

    def _log(
        self,
        log_depth: int,
        message: str,
        log: bool = False,
        indent: str = "    ",
    ) -> None:
        """Indented debug logger with timestamp support."""
        if not log:
            return
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        print(f"[{timestamp}] {indent * log_depth}{message}")


class TicketSystem:
    """Coordinates multiple Ticket instances to deduce global field mappings."""

    def __init__(
        self,
        field_rules: dict[str, list[list[int]]],
        tickets: list[Ticket],
        my_ticket: Ticket,
    ) -> None:
        self.field_rules = field_rules
        self.other_tickets = tickets
        self.my_ticket = my_ticket
        self.valid_tickets: list[Ticket] = []
        self.global_field_candidates: dict[int, set[str]] = {}
        self.global_value_candidates: dict[str, set[int]] = {}
        self.global_fields: dict[str, int] = {}

    def summarize_invalid_tickets(
        self,
        exclusive: bool = True,
        log: bool = False,
        log_depth: int = 0,
    ) -> int:
        """Run non-exclusive evaluation on all tickets and return sum of invalid values."""
        self._log(log_depth, "Evaluating my ticket", log=log)
        self.my_ticket.evaluate_values(
            exclusive=exclusive, log=log, log_depth=log_depth + 1
        )

        for i, ticket in enumerate(self.other_tickets):
            self._log(log_depth, f"Evaluating ticket {i}", log=log)
            ticket.evaluate_values(
                exclusive=exclusive, log=log, log_depth=log_depth + 1
            )

        return sum(sum(t.invalid_values) for t in self.other_tickets)

    def filter_valid_tickets(
        self,
        log: bool = False,
        log_depth: int = 0,
    ) -> None:
        """Run exclusive evaluation on all tickets and keep only valid ones."""
        self._log(log_depth, "Filtering valid tickets", log=log)
        self.summarize_invalid_tickets(
            exclusive=True, log=log, log_depth=log_depth + 1
        )

        for i, ticket in enumerate(self.other_tickets):
            self._log(log_depth + 1, f"Checking validity of ticket {i}", log=log)
            if ticket.valid_ticket:
                self.valid_tickets.append(ticket)

    def identify_mapping(
        self,
        log: bool = False,
        log_depth: int = 0,
    ) -> None:
        """Initialize search space and then iteratively refine the mapping."""
        self._aggregate_candidates(log=log, log_depth=log_depth)
        self._refine_candidates(log=log, log_depth=log_depth)

    def _aggregate_candidates(
        self,
        log: bool = False,
        log_depth: int = 0,
    ) -> None:
        """Find compatible candidates for each field and value."""
        self._log(
            log_depth,
            "Identifying initial set of possible fields for each value",
            log=log,
        )

        for value in self.my_ticket.values:
            self.global_field_candidates[value] = self.my_ticket.field_candidates[
                value
            ].intersection(
                *[ticket.field_candidates[value] for ticket in self.valid_tickets]
            )

        for field in self.my_ticket.field_rules:
            self.global_value_candidates[field] = self.my_ticket.value_candidates[
                field
            ].intersection(
                *[ticket.value_candidates[field] for ticket in self.valid_tickets]
            )

    def _refine_candidates(
        self,
        log: bool = False,
        log_depth: int = 0,
    ) -> None:
        """Iteratively reduce the set of compatible pairs."""
        self._log(log_depth, "Refining candidates", log=log)
        self._try_to_refine_fields(log=log, log_depth=log_depth + 1)
        self._try_to_refine_values(log=log, log_depth=log_depth + 1)

    def _try_to_refine_fields(
        self,
        log: bool = False,
        log_depth: int = 0,
    ) -> None:
        """Try to identify fields with only one possible value."""
        identified_fields = [
            field
            for field in self.global_value_candidates
            if len(self.global_value_candidates[field]) == 1
        ]
        if identified_fields:
            self._log(
                log_depth,
                f"Identified fields ready for pruning {identified_fields}",
                log=log,
            )
            pruned_field = identified_fields.pop()
            self._prune_field(pruned_field, log=log, log_depth=log_depth + 1)

    def _try_to_refine_values(
        self,
        log: bool = False,
        log_depth: int = 0,
    ) -> None:
        """Try to identify values with only one possible field."""
        identified_values = [
            value
            for value in self.global_field_candidates
            if len(self.global_field_candidates[value]) == 1
        ]
        if identified_values:
            self._log(
                log_depth,
                f"Identified values ready for pruning {identified_values}",
                log=log,
            )
            pruned_value = identified_values.pop()
            self._prune_value(pruned_value, log=log, log_depth=log_depth + 1)

    def _prune_field(
        self,
        pruned_field: str,
        log: bool = False,
        log_depth: int = 0,
    ) -> None:
        """Assign field to value and prune it from the search space."""
        pruned_value = next(iter(self.global_value_candidates[pruned_field]))
        self._log(
            log_depth,
            f"Pruning field '{pruned_field}' (maps to value {pruned_value})",
            log=log,
        )

        self.global_fields[pruned_field] = pruned_value
        del self.global_value_candidates[pruned_field]

        for field in list(self.global_value_candidates):
            self.global_value_candidates[field].discard(pruned_value)

        del self.global_field_candidates[pruned_value]
        self._refine_candidates(log=log, log_depth=log_depth + 1)

    def _prune_value(
        self,
        pruned_value: int,
        log: bool = False,
        log_depth: int = 0,
    ) -> None:
        """Assign value to field and prune it from the search space."""
        pruned_field = next(iter(self.global_field_candidates[pruned_value]))
        self._log(
            log_depth,
            f"Pruning value {pruned_value} (maps to field '{pruned_field}')",
            log=log,
        )

        self.global_fields[pruned_field] = pruned_value
        del self.global_field_candidates[pruned_value]

        for value in list(self.global_field_candidates):
            self.global_field_candidates[value].discard(pruned_field)

        del self.global_value_candidates[pruned_field]
        self._refine_candidates(log=log, log_depth=log_depth + 1)

    def _log(
        self,
        log_depth: int,
        message: str,
        log: bool = False,
        indent: str = "    ",
    ) -> None:
        """Indented debug logger with timestamp support."""
        if not log:
            return
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        print(f"[{timestamp}] {indent * log_depth}{message}")


TicketData: TypeAlias = tuple[
    dict[str, list[list[int]]], Ticket, list[list[int]]
]


def read_input(file_path: str | Path = "input.txt") -> TicketData:
    """Parse and validate ticket data from the input file."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    content = path.read_text().strip()
    if not content:
        raise ValueError(f"Input file is empty: {path}")

    parts = content.split("\n\n")
    if len(parts) != 3:
        raise ValueError(
            f"Unexpected input format in {path}. "
            "Expected 3 sections separated by blank lines."
        )

    raw_rules, raw_my, raw_others = parts

    if not raw_my.startswith("your ticket") or not raw_others.startswith(
        "nearby tickets"
    ):
        raise ValueError("Missing expected section headers in input file.")

    field_rules: dict[str, list[list[int]]] = {}
    for line in raw_rules.splitlines():
        if ": " not in line:
            raise ValueError(f"Malformed rule line: {line}")
        name, ranges_str = line.split(": ")
        ranges = [[int(x) for x in r.split("-")] for r in ranges_str.split(" or ")]
        field_rules[name] = ranges

    my_ticket = Ticket(
        field_rules, [int(x) for x in raw_my.splitlines()[1].split(",")]
    )
    other_tickets = [
        [int(x) for x in t.split(",")]
        for t in raw_others.split(":\n")[1].splitlines()
    ]

    return field_rules, my_ticket, other_tickets


def main() -> None:
    field_rules, my_ticket, other_tickets = read_input(
        "./solutions/2020/day-16/input.txt"
    )
    tickets = [Ticket(field_rules, ticket) for ticket in other_tickets]
    ticket_system = TicketSystem(field_rules, tickets, my_ticket)

    part1 = ticket_system.summarize_invalid_tickets()
    print(f"Part 1: {part1}")

    ticket_system.filter_valid_tickets()
    ticket_system.identify_mapping()

    departure_values = [
        ticket_system.my_ticket.values[ticket_system.global_fields[field]]
        for field in ticket_system.global_fields
        if field.startswith("departure")
    ]
    print(f"Part 2: {math.prod(departure_values)}")


if __name__ == "__main__":
    main()
