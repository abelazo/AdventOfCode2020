
class Person:

    def __init__(self, answers):
        self._answers = answers

    def __repr__(self):
        return "a:{}".format(self._answers)

    def __str__(self):
        return "a:{}".format(self._answers)
