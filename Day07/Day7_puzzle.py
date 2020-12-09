from rules import Rule


def get_candidates(rules, color):
    candidates = set()
    for r in rules:
        if r.allowed(color):
            candidates.add(r)
    return candidates


def get_containers(rules, color, collector):
    collector.add(color)
    containers = [rule.get_bag() for rule in get_candidates(rules, color)]
    #print("Containers of {} are {}".format(color, containers))
    if containers is None or len(containers) == 0:
        return collector
    else:
        for element in containers:
            new_containers = get_containers(rules, element, collector)
            #print("{} has the these new containers: {}".format(element, new_containers))
            if new_containers is not None:
                collector = collector.union(set(new_containers))
        return collector

    
def solve_1(bag_type, rules):
    res = set()
    containers = get_containers(rules, bag_type, res)
    containers.remove(bag_type) # TODO: This could be improved
    print("The number of bags that can contain '{}' is {}".format(bag_type, len(containers)))


def get_num_bags(num_bags, rule, rules):
    #print ("Evaluating {}".format(rule))
    content = rule.get_content()
    
    if content is None or content == {}:
        return num_bags
    else:
        cumul = num_bags
        for element in content:
            num_contents = int(content[element])
            jander = (num_bags * num_contents)
            element_rule = [item for item in rules if item.get_bag() == element][0]
            cumul += get_num_bags(jander, element_rule, rules)
            #print ("Value of cumul afer processing {}: {}".format(element, cumul))
        #print ("Value of cumul {}".format(cumul))
        return cumul

def solve_2(bag_type, rules):
    shiny_gold_rule = [item for item in rules if item.get_bag() == bag_type][0]
    contained_bags = get_num_bags(1, shiny_gold_rule, rules) - 1
    print("The number of bags within a '{}' is {}".format(bag_type, contained_bags))
    
    
if __name__ == '__main__':
    with open('Rules.txt') as f:
        all_rules = [Rule(line.strip()) for line in f.readlines()]

    bag_type = "shiny gold"

    solve_1(bag_type, all_rules)
    solve_2(bag_type, all_rules)
