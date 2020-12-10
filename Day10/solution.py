
def get_device_joltage(joltages):
    return max(joltages) + 3

def get_valid_candidates(candidates, current_joltage):
    candidates.sort()
    valid_candidates = [c for c in candidates if current_joltage < c and c <= current_joltage + 3]
    return valid_candidates

def get_differences(joltages):
    target_joltage = get_device_joltage(joltages)
    joltages.append(target_joltage)
    joltages.sort()
    current_joltage = 0
    ones = set()
    threes = set()
    for j in joltages:
        if (j - current_joltage) == 1:
            ones.add(j)
        else:
            threes.add(j)
        current_joltage = j
    return ones, threes

def solve_1(joltages):
    ones, threes = get_differences(joltages)
    return (len(ones) * len(threes))

def solve_2(joltages):
    pass

if __name__ == '__main__':
    with open('Joltages.txt') as f:
        adapters = [int(line.strip()) for line in f.readlines()]

    s = solve_1(adapters)
    print("Solution 1 is {}".format(s))
