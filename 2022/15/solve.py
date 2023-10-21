import functools
import re
import time
from pathlib import Path


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value

    return wrapper_timer


def manhattan_distance(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x1 - x2) + abs(y1 - y2)


class Sensor:
    def __init__(self, definition: str) -> None:
        sensor_def, beacon_def = definition.split(":")

        self.own_coordinates = self.get_x_y(sensor_def)
        self.closest_beacon = self.get_x_y(beacon_def)

        self.sensing_range = manhattan_distance(
            *self.own_coordinates, *self.closest_beacon
        )

    @staticmethod
    def get_x_y(definition: str) -> tuple[int, int]:
        x_pattern = re.compile("(?<=x=)-?[0-9]*")
        x_match = re.search(x_pattern, definition)

        if not x_match:
            raise ValueError(f"{definition} appears to not have 'x'")
        x_pos = int(x_match.group(0))

        y_pattern = re.compile("(?<=y=)-?[0-9]*")
        y_match = re.search(y_pattern, definition)

        if not y_match:
            raise ValueError(f"{definition} appears to not have 'y'")
        y_pos = int(y_match.group(0))

        return x_pos, y_pos


@timer
def covered_positions(
    sensors: list[Sensor], row: int, limit_min: int, limit_max: int
) -> set[int]:
    covered: set[int] = set()

    last_x: int = limit_min - 1

    for sensor in sensors:
        if abs(sensor.own_coordinates[1] - row) > sensor.sensing_range:
            continue

        distance_to_row = abs(sensor.own_coordinates[1] - row)
        remaining_range = sensor.sensing_range - distance_to_row

        if sensor.own_coordinates[0] + remaining_range + 1 <= last_x:
            continue

        sensor_range_in_row = list(
            range(
                max(sensor.own_coordinates[0] - remaining_range, last_x + 1),
                min(sensor.own_coordinates[0] + remaining_range, limit_max) + 1,
            )
        )

        if len(sensor_range_in_row):
            last_x = sensor_range_in_row[-1]

        covered_by_sensor = set(sensor_range_in_row)
        # if sensor.closest_beacon[1] == row:
        #     covered_by_sensor.remove(sensor.closest_beacon[0])
        covered.update(covered_by_sensor)

    return covered


def find_noncovered(
    sensors: list[Sensor], row: int, limit_min: int, limit_max: int
) -> int:
    begin = limit_min

    for i, sensor in enumerate(sensors):
        distance_to_row = abs(sensor.own_coordinates[1] - row)

        if distance_to_row > sensor.sensing_range:
            continue

        # print(begin)

        remaining_range = abs(sensor.sensing_range - distance_to_row)

        if sensor.own_coordinates[0] - remaining_range > begin:
            new_begin = find_noncovered(sensors[i + 1 :], row, begin, limit_max)

            if new_begin == begin:
                return begin

            begin = new_begin

        if min(sensor.own_coordinates[0] + remaining_range, limit_max) < begin:
            continue

        begin = min(sensor.own_coordinates[0] + remaining_range + 1, limit_max)

    return begin


@timer
def find_beacon(
    sensors: list[Sensor], min_coord: int, max_coord: int
) -> tuple[int, int]:
    for y in range(min_coord, max_coord + 1):
        x: int = find_noncovered(sensors, y, min_coord, max_coord)

        if x < max_coord:
            return x, y

    raise Exception("Distress beacon not found!!!")


if __name__ == "__main__":
    sensors = []

    INPUT_FILE = "input_ex.txt"
    CHECKED_ROW: int = 10
    MIN_COORD = 0
    MAX_COORD = 20

    CHECKED_ROW: int = 2000000
    INPUT_FILE = "input.txt"
    MAX_COORD = 4000000

    with open(Path(__file__).parent / INPUT_FILE) as input_file:
        for line in input_file.readlines():
            sensors.append(Sensor(line))

    sensors.sort(key=lambda sensor: sensor.own_coordinates[0])

    # print(len(covered_positions(sensors, 362324, MIN_COORD, MAX_COORD))) # PART 1

    beacon_coords = find_beacon(sensors, MIN_COORD, MAX_COORD)

    print(beacon_coords)
    print(beacon_coords[0] * 4000000 + beacon_coords[1])
