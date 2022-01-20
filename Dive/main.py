INPUT_PATH = "Dive/input.txt"
OUTPUT_PATH = "Dive/output.txt"

def part_one(data):
    horizontal = 0
    depth = 0
    for command in data:
        match command[0]:
            case "forward":
                horizontal += command[1]
            case "up":
                depth -= command[1]
            case "down":
                depth += command[1]
    return horizontal * depth

def part_two(data):
    horizontal = 0
    depth = 0
    aim = 0

    for command in data:
        match command[0]:
            case "forward":
                horizontal += command[1]
                depth += command[1] * aim
            case "up":
                aim -= command[1]
            case "down":
                aim += command[1]
    return horizontal * depth

if __name__ == "__main__":
    with open(INPUT_PATH, "r") as f:
        raw_data = f.read().split()
    data = []
    for i in range(len(raw_data)):
        if i % 2 == 0:
            data.append([raw_data[i], raw_data[i + 1]])
    for command in data:
        command[1] = int(command[1])
    with open(OUTPUT_PATH, "w") as f:
        f.write(f"PART ONE: {part_one(data)}\nPART TWO: {part_two(data)}")
