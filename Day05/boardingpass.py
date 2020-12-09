
def _calculate_seat_id(row, column):
    return _calculate_row(row) * 8 + _calculate_column(column)

def _calculate_row(row):
    seat = 0
    iteration = 0
    for action in row:
        current_half = pow(2,6-iteration)
        if action == 'B':
            seat += current_half
        iteration+=1
    return seat

def _calculate_column(column):
    seat = 0
    iteration = 0
    for action in column:
        current_half = pow(2,2-iteration)
        if action == 'R':
            seat += current_half
        iteration+=1
    return seat


class Pass:
    def __init__(self, definition):
        self._row = definition[0:7]
        self._column = definition[7:10]
        self._seat_id = _calculate_seat_id(self._row, self._column)

    def __repr__(self):
        return "r:{}|c:{}|sid:{}".format(self._row, self._column, self._seat_id)
    def __str__(self):
        return "r:{}|c:{}|sid:{}".format(self._row, self._column, self._seat_id)

    def get_seat_id(self):
        return self._seat_id

if __name__ == "__main__":
    
    print(_calculate_row("BFFFBBF"))
    print(_calculate_column("RRR"))
    print()
    print(_calculate_row("FFFBBBF"))
    print(_calculate_column("RRR"))
    print()
    print(_calculate_row("BBFFBBF"))
    print(_calculate_column("RLL"))
    
