# https://adventofcode.com/2022/day/3

def get_item_priority(item: str):
    char = item[0]

    if char.isupper():
        return ord(char) - 64 + 26
    if char.islower():
        return ord(char) - 96
    
    raise ValueError("Not a viable ascii character")

def main():
    duplicates = []

    with open("./2022/Day_3/input.txt", "r") as input_file:
        for line in input_file.readlines():
            line = line.strip('\n')
            middle = int(line.__len__() / 2)

            compartment_one, compartment_two = line[:middle], line[middle:]

            for item in compartment_one:
                if item in compartment_two:
                    duplicates.append(item)
                    break
            
    # print(duplicates)
    print(sum([get_item_priority(item) for item in duplicates]))  # correct out - 8202

if __name__ == "__main__":
    main()