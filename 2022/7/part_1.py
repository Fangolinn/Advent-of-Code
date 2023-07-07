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
    
    if parent_dir.size <= max_size:
        return [parent_dir]

    dirs = []
    for dir in parent_dir.child_dirs:
        dirs.extend(find_dirs_of_max_size(dir, max_size))

    return dirs

def main():
    filesystem = Directory(name="/", parent_dir=None)
    current_dir = filesystem
    with open(Path(__file__).parent / "input.txt") as input_file:
        for line in input_file.readlines():
            if line == "\n":
                break
            line = line.split()
            if line[0] == '$':
                if line[1] == "cd":
                    if line[2] == "..":
                        current_dir = current_dir.parent_dir
                        continue
                    current_dir = change_dir(current_dir, line[2])
                if line[1] == "ls":
                    continue
                continue

            if line[0] == "dir":
                current_dir.child_dirs.append(Directory(name=line[1], parent_dir=current_dir))
                continue

            current_dir.files.append(File(name=line[1], size=int(line[0])))
            
    return([dir for dir in find_dirs_of_max_size(filesystem, 100000)])


if __name__ == "__main__":
    print(main())
