from __future__ import annotations

from io import TextIOWrapper
from pathlib import Path

from parse import parse


class Valve:
    def __init__(self, name: str, flow_rate: int) -> None:
        self.name: str = name
        self.flow_rate: int = flow_rate
        self.is_open: bool = flow_rate == 0
        self.connected_valves: set[Valve] = set()

    def __str__(self) -> str:
        return f"{self.name} {self.flow_rate} {[valve.name for valve in self.connected_valves]}"


def parse_input(input: TextIOWrapper) -> tuple[dict[str, Valve], dict[str, list[str]]]:
    """
    Parse input to a graph, return the node for AA valve.
    """
    valves: dict[str, Valve] = dict()
    connections: dict[str, list[str]] = dict()

    for line in input.readlines():
        parsed_valve = parse("Valve {name} has flow rate={flow_rate};{remainder}", line)

        valves[parsed_valve["name"]] = Valve(
            parsed_valve["name"], int(parsed_valve["flow_rate"])
        )

        parsed_connections: list[str] = (
            str(parsed_valve["remainder"]).replace(",", "").split()[4:]
        )
        connections[parsed_valve["name"]] = parsed_connections

    return valves, connections


def create_graph(
    valves: dict[str, Valve], connections: dict[str, list[str]], start_node: str = "AA"
) -> Valve:
    for valve_name, valve_connections in connections.items():
        for connected_valve in valve_connections:
            valves[valve_name].connected_valves.add(valves[connected_valve])

    return valves[start_node]


def release_most_pressure(
    current_valve: Valve,
    time_left: int,
    current_flow: int = 0,
    released_pressure: int = 0,
) -> int:
    released_pressure += current_flow if time_left != 0 else 0

    if time_left == 0 or time_left == 1:
        # print(f"Released pressure: {released_pressure}")
        return released_pressure

    max_released: int = 0

    for next_valve in current_valve.connected_valves:
        max_released = max(
            max_released,
            release_most_pressure(
                next_valve,
                time_left - 1,
                current_flow,
                released_pressure,
            ),
        )

    if not current_valve.is_open:
        current_valve.is_open = True
        time_left -= 1
        for next_valve in current_valve.connected_valves:
            max_released = max(
                max_released,
                release_most_pressure(
                    next_valve,
                    time_left - 1,
                    current_flow + current_valve.flow_rate,
                    released_pressure,
                ),
            )
        current_valve.is_open = False

    return max_released


if __name__ == "__main__":
    INPUT_FILE = "input_ex.txt"
    TIME_LEFT: int = 30

    with open(Path(__file__).parent / INPUT_FILE) as input_file:
        valves, connections = parse_input(input_file)

    valves_graph: Valve = create_graph(valves, connections)

    print(release_most_pressure(valves_graph, TIME_LEFT))
