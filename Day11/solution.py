

class Point:
    FLOOR = "."
    EMPTY = "L"
    OCCUPIED = "#"

    def __init__(self, x, y, status):
        self._x = x
        self._y = y
        self._status = status
        self._context = []

    def __str__(self):
        #return "s:{}|c:{}".format(self._status, len(self._context))
        return "{}".format(self._status)

    def __repr__(self):
        #return "s:{}|c:{}".format(self._status, len(self._context))
        return "{}".format(self._status)
    
    def set_context(self, context):
        self._context = context.copy()

    def get_status(self):
        return str(self._status)

    def new_status(self):
        num_occupied_seats = len([s for s in self._context if s.get_status() == Point.OCCUPIED])
        if self.get_status() == Point.EMPTY and num_occupied_seats == 0:
            return Point.OCCUPIED
        elif(self.get_status() == Point.OCCUPIED and num_occupied_seats >= 4):
            return Point.EMPTY
        else:
            return self.get_status()

def generate_points(seats):
    ret = []
    for r in range(len(seats)):
        ret.append([])
        row = seats[r]
        for c in range(len(row)):
            status = row[c]
            p = Point(r, c, status)
            ret[r].append(p)
    return ret


def get_context(points, r, c):
    context = []
    # previous row
    if r-1 >= 0:
        prev_row = points[r-1]
        if c-1 >= 0: context.append(prev_row[c-1])
        context.append(prev_row[c])
        if c+1 < len(prev_row): context.append(prev_row[c+1])

    # current row
    curr_row = points[r]
    if c-1 >= 0: context.append(curr_row[c-1])
    # context.append(curr_row[c])
    if c+1 < len(curr_row): context.append(curr_row[c+1])

    # next row
    if r+1 < len(points):
        next_row = points[r+1]
        if c-1 >= 0: context.append(next_row[c-1])
        context.append(next_row[c])
        if c+1 < len(next_row): context.append(next_row[c+1])

    return context
    
def initialize_contexts(points):
    for r in range(len(points)):
        for c in range(len(points[r])):
            context = get_context(points, r, c)
            points[r][c].set_context(context)


def apply_rules(points):
    new_points = []
    for r in range(len(points)):
        new_points.append([])
        for c in range(len(points[r])):
            p = Point(r,c, points[r][c].new_status())
            new_points[r].append(p)
    return new_points


def equals(state1, state2):
    equals = True
    for r in range(len(state1)):
        for c in range(len(state1[r])):
            equals = equals and state1[r][c].get_status() == state2[r][c].get_status()
    return equals

def solve_1(seats):
    points = generate_points(seats)
    initialize_contexts(points)

    curr_points = points
    new_points = []
    isDifferent = True
    while isDifferent:
        new_points = apply_rules(curr_points)
        initialize_contexts(new_points)
        isDifferent = not equals(curr_points, new_points)
        curr_points = new_points

    counter = 0
    for r in range(len(curr_points)):
        for c in range(len(curr_points[r])):
            if (curr_points[r][c].get_status() == Point.OCCUPIED): counter += 1
    return counter

def solve_2(seats):
    return None


if __name__ == '__main__':
    with open('Seats.txt') as f:
        seats = [(line.strip()) for line in f.readlines()]

    print("Solution to 1 is {}".format(solve_1(seats)))
    print("Solution to 2 is {}".format(solve_2(seats)))
