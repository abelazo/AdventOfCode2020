def _get_color(definition):
    return definition.split("contain")[0].strip().replace(" bags", "")


def _get_content(definition):
    return [x.strip().replace(" bags", "").replace(" bag", "") for x in
            definition.split("contain")[1].strip()[0:-1].split(',')]


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


