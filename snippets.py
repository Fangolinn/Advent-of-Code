import functools
import time
from pathlib import Path

INPUT_FILE = "input_ex.txt"
with open(Path(__file__).parent / INPUT_FILE) as input_file:
    pass

if __name__ == "__main__":
    ...


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
