
def isXmable(candidate, subset):
    for i in subset:
        #print("Now with {}".format(i))
        for n in subset:
            if i+n == candidate:
                return True
    return False


def solve_1(xmas, size):
    i = size
    candidate = xmas[i]
    subset = xmas[i-size:i]
    while isXmable(candidate,subset):
        candidate = xmas[i]
        subset = xmas[i-size:i]
        i += 1
    return candidate

def solve_2(xmas, weakness):
    i = 0
    found = False
    while not found and i < len(xmas):
        candidate = xmas[i]
        cumul = candidate
        collector = [candidate]
        for j in xmas[i+1:]:  # Find friends
            cumul += j
            collector.append(j)
            if cumul == weakness:
                collector.sort()
                return collector
            elif cumul > weakness: # Not found. Continue
                break;
        i += 1


if __name__ == '__main__':
    with open('Xmas.txt') as f:
        xmas = [int(line.strip()) for line in f.readlines()]

    preamble_size = 25
    weakness = solve_1(xmas, preamble_size)
    print ("First number not being at least one sum of two previous {} is {}".format(preamble_size, weakness))

    subset_2 = [n for n in xmas if n < weakness]
    solution = solve_2(subset_2, weakness)
    print("The weakness is: {}".format(solution[0] + solution[-1]))

# if __name__ == '__main__':
#     xmas = [35,
#             20,
#             15,
#             25,
#             47,
#             40,
#             62,
#             55,
#             65,
#             95,
#             102,
#             117]
#     ret = solve_2(xmas, 127)
#     print(ret)
 
