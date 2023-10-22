from __future__ import annotations

import re
from io import TextIOWrapper
from pathlib import Path


class Valve:
    def __init__(self, flow_rate: int, connected_valve: Valve | None = None) -> None:
        self.flow_rate = flow_rate
        self.connected_valves: set[Valve] = (
            set([connected_valve]) if connected_valve else set()
        )


def parse_input(input: TextIOWrapper) -> dict[str, Valve]:
    valves: dict[str, Valve] = dict()

    for line in input.readlines():
        valve_name_match = re.search(re.compile("(?<=(Valve ))[A-Z]+"), line)
        if not valve_name_match:
            raise ValueError(f"{line} appears to not have valve name!!!")
        valve_name = valve_name_match.group(0)

        flow_rate_match = re.search(re.compile("(?<=(rate=))[0-9]+"), line)
        if not flow_rate_match:
            raise ValueError(f"{line} appears to not have flow rate!!!")
        flow_rate = int(flow_rate_match.group(0))

        connected_valves_match = re.search(re.compile("(?<=(to valve)).+$"), line)
        if not connected_valves_match:
            raise ValueError(f"{line} appears to not have connected valves!!!")
        connected_valves = (
            connected_valves_match.group(0)
            .removeprefix("s")
            .replace(" ", "")
            .split(",")
        )

        valves[valve_name] = Valve(flow_rate=flow_rate)

    return dict()


if __name__ == "__main__":
    INPUT_FILE = "input_ex.txt"

    with open(Path(__file__).parent / INPUT_FILE) as input_file:
        valves = parse_input(input_file)
