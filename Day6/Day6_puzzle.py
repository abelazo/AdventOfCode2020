
def per_section(it, is_delimiter=lambda x: x.isspace()):
    ret = []
    for line in it:
        if is_delimiter(line):
            if ret:
                yield ret  # OR  ''.join(ret)
                ret = []
        else:
            ret.append(line.rstrip())  # OR  ret.append(line)
    if ret:
        yield ret

def get_groups(file):
    with open(file) as f:
        sections = list(per_section(f))
    return sections     

def split(answers):
    return [answer for answer in answers]

def solve_1(groups):
    total=0
    for g in groups:
        group_answers = "".join(g)
        different_answers="".join(set(group_answers))
        total += len(different_answers)
    print("Total number of different answers: {}".format(total))
    
def solve_2(groups):
    total = 0
    for group in groups:
        separated_answers = [set(split(answers)) for answers in group]
        total += len(set.intersection(*separated_answers))
    print("Total number of YES answers in all elements: {}".format(total))
    
groups = get_groups('Answers.txt')
solve_1(groups)
solve_2(groups)
