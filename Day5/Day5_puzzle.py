from boardingpass import Pass

with open('BoardingPasses.txt') as f:
    bps = [Pass(line.strip()) for line in f.readlines()]

ids = [bp.get_seat_id() for bp in bps]
ids.sort()
expected=list(range(ids[0], ids[-1], 1))

print("Max Seat ID: {}".format(ids[-1]))
print("Empty seats: {}".format(set(ids).symmetric_difference(set(expected))))
