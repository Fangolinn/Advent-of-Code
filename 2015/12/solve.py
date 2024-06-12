import json


def sum_with_python(data: dict | list | int | str) -> int:
    numbers_sum: int = 0

    match data:
        case int():
            return data
        case dict():
            for value in data.values():
                numbers_sum += sum_with_python(value)
        case list():
            for item in data:
                numbers_sum += sum_with_python(item)
        case str():
            pass
        case _:
            raise ValueError("Unexpected 'data' type", type(data))

    return numbers_sum


def sum_with_python_part2(data: dict | list | int | str) -> int:
    numbers_sum: int = 0

    match data:
        case int():
            return data
        case dict():
            if "red" not in data.values():
                for value in data.values():
                    numbers_sum += sum_with_python_part2(value)
        case list():
            for item in data:
                numbers_sum += sum_with_python_part2(item)
        case str():
            pass
        case _:
            raise ValueError("Unexpected 'data' type", type(data))

    return numbers_sum


if __name__ == "__main__":
    with open("input.json") as file:
        data: dict | list = json.load(file)

    print(sum_with_python(data))
    print(sum_with_python_part2(data))
