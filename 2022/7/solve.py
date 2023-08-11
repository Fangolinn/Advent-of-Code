# https://adventofcode.com/2022/day/7

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class Directory:
    name: str
    parent_dir: Optional[Directory]
    child_dirs: list[Directory] = field(default_factory=list)
    files: list[File] = field(default_factory=list)

    @property
    def size(self) -> int:
        return self.files_size + self.child_dirs_size

    @property
    def files_size(self) -> int:
        return sum([file.size for file in self.files])

    @property
    def child_dirs_size(self) -> int:
        return sum([(dir.files_size + dir.child_dirs_size) for dir in self.child_dirs])


@dataclass
class File:
    name: str
    size: int


def change_dir(parent_dir: Directory, name: str) -> Directory:
    if name == parent_dir.name and name == "/":
        return parent_dir

    return [dir for dir in parent_dir.child_dirs if dir.name == name][0]


def find_dirs_of_max_size(parent_dir: Directory, max_size: int) -> list[Directory]:
    if parent_dir.size == 0:
        return []

    dirs = []
    if parent_dir.size <= max_size:
        dirs.append(parent_dir)

    for dir in parent_dir.child_dirs:
        dirs.extend(find_dirs_of_max_size(dir, max_size))

    return dirs


def process_input(filesystem: Directory) -> None:
    current_dir = filesystem
    with open(Path(__file__).parent / "input.txt") as input_file:
        for line in input_file.readlines():
            if line == "\n":
                break
            line = line.split()
            if line[0] == "$":
                if line[1] == "cd":
                    if line[2] == "..":
                        current_dir = current_dir.parent_dir
                        continue
                    current_dir = change_dir(current_dir, line[2])
                if line[1] == "ls":
                    continue
                continue

            if line[0] == "dir":
                current_dir.child_dirs.append(
                    Directory(name=line[1], parent_dir=current_dir)
                )
                continue

            current_dir.files.append(File(name=line[1], size=int(line[0])))


def find_dirs_of_min_size(parent_dir: Directory, max_size: int) -> list[Directory]:
    if parent_dir.size == 0:
        return []

    dirs = []
    if parent_dir.size >= max_size:
        dirs.append(parent_dir)

    for dir in parent_dir.child_dirs:
        dirs.extend(find_dirs_of_min_size(dir, max_size))

    return dirs


def main_part1():
    filesystem = Directory(name="/", parent_dir=None)
    process_input(filesystem)

    return sum([dir.size for dir in find_dirs_of_max_size(filesystem, 100000)])


def main_part2():
    TOTAL_SIZE = 70000000
    REQUIRED_SIZE = 30000000

    filesystem = Directory(name="/", parent_dir=None)
    process_input(filesystem)

    # How much space do we need to free?
    free_space = TOTAL_SIZE - filesystem.size
    missing_space = REQUIRED_SIZE - free_space

    # Find dirs that are bigger than required space to free
    dirs = find_dirs_of_min_size(filesystem, missing_space)

    # Get the smallest one and return it's size
    return sorted(dirs, key=lambda dir: dir.size)[0].size


if __name__ == "__main__":
    print(main_part2())
