INPUT_PATH = "SonarSweep/input.txt"
OUTPUT_PATH = "SonarSweep/output.txt"

def part_one(data):
    increase_amount = 0
    for i in range(len(data)):
        if data[i] > data[i-1] and i != 0:
            increase_amount += 1
    return increase_amount

def part_two(data):
    class SlidingWindow:
        def __init__(self, point_num):
            self.point_num = point_num
            self.values = []
        
        @property
        def line_nums(self):
            return [self.point_num, self.point_num+1, self.point_num+2]
        
        @property
        def total(self):
            return sum(self.values)

    sliding_windows = []
    for i in range(len(data)):
        sliding_windows.append(SlidingWindow(i))
        for window in sliding_windows:
            if i in window.line_nums:
                window.values.append(data[i])
    print(len(sliding_windows))
    for window in sliding_windows:
            if len(window.values) != 3:
                sliding_windows.remove(window)

    totals = []
    for window in sliding_windows:
        totals.append(window.total)
    return part_one(totals)

if __name__ == "__main__":
    with open(INPUT_PATH, "r") as f:
        data = list(map(int, f.read().split()))
    with open(OUTPUT_PATH, "w") as f:
        f.write(f"PART ONE: {part_one(data)}\nPART TWO: {part_two(data)}")
