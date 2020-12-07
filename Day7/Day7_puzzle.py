from rules import Rule


def get_candidates(rules, color):
    candidates = set()
    for r in rules:
        if r.allowed(color):
            candidates.add(r)
    return candidates


def extract_candidates(rules, color, collector):
    collector.add(color)
    containers = [rule.get_bag() for rule in get_candidates(rules, color)]
    #print("Containers of {} are {}".format(color, containers))
    if containers is None or len(containers) == 0:
        return collector
    else:
        for element in containers:
            #print("Checking {}".format(element))
            new_containers = extract_candidates(rules, element, collector)
            #print("New containers: {}".format(new_containers))
            if new_containers is not None:
                collector = collector.union(set(new_containers))
        return collector

def solve_1(bag_type, rules):
    res = set()
    containers = extract_candidates(rules, bag_type, res)
    containers.remove(bag_type) # This could be improved
    print("The number of bags that can contain '{}' is {}: \n{}".format(bag_type, len(containers), containers))

if __name__ == '__main__':
    with open('Rules.txt') as f:
        all_rules = [Rule(line.strip()) for line in f.readlines()]

    bag_type = "shiny gold"
    solve_1(bag_type, all_rules)

# if __name__ == '__other__':
#     other_rules = [Rule("light red bags contain 1 bright white bag, 2 muted yellow bags."),
#                    Rule("dark orange bags contain 3 bright white bags, 4 muted yellow bags."),
#                    Rule("bright white bags contain 1 shiny gold bag."),
#                    Rule("muted yellow bags contain 2 shiny gold bags, 9 faded blue bags."),
#                    Rule("shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags."),
#                    Rule("dark olive bags contain 3 faded blue bags, 4 dotted black bags."),
#                    Rule("vibrant plum bags contain 5 faded blue bags, 6 dotted black bags."),
#                    Rule("faded blue bags contain no other bags."), Rule("dotted black bags contain no other bags.")]
#     start = "shiny gold"
#     print("The number of bags that can contain {} is {}".format(start, len(extract_candidates(other_rules, start, res))))
