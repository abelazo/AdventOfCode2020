def _get_color(definition):
    return definition.split("contain")[0].strip().replace(" bags", "")


def _get_content(definition):
    raw_content = [x.strip().replace(" bags", "").replace(" bag", "") for x in
            definition.split("contain")[1].strip()[0:-1].split(',')]
    content = {}
    for bag in raw_content:
        if bag != "no other":
            amount = bag.split(' ')[0].strip()
            color = bag.split(' ',1)[1].strip()
            content[color] = amount
    return content

class Rule:
    def __init__(self, definition):
        self._bag = _get_color(definition)
        self._content = _get_content(definition)

    def __repr__(self):
        return "b:{}|c:{}".format(self._bag, self._content)

    def __str__(self):
        return "b:{}|c:{}".format(self._bag, self._content)

    def get_content(self):
        return self._content

    def get_bag(self):
        return self._bag

    def allowed(self, color):
        return any([color in c for c in self._content])


if __name__ == '__main__':
     other_rules = [Rule("light red bags contain 1 bright white bag, 2 muted yellow bags."),
                    Rule("dark orange bags contain 3 bright white bags, 4 muted yellow bags."),
                    Rule("bright white bags contain 1 shiny gold bag."),
                    Rule("muted yellow bags contain 2 shiny gold bags, 9 faded blue bags."),
                    Rule("shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags."),
                    Rule("dark olive bags contain 3 faded blue bags, 4 dotted black bags."),
                    Rule("vibrant plum bags contain 5 faded blue bags, 6 dotted black bags."),
                    Rule("faded blue bags contain no other bags."), Rule("dotted black bags contain no other bags.")]
     print(other_rules)
