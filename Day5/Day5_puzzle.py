from boardingpass import Pass

with open('BoardingPasses.txt') as f:
    bps = [Pass(line.strip()) for line in f.readlines()]

max_bp = 0
for bp in bps:
    if (bp.get_seat_id() > max_bp):
        max_bp = bp.get_seat_id()

print("Max Seat ID: {}".format(max_bp))

ids = [bp.get_seat_id() for bp in bps]
ids.sort()

expected=list(range(ids[0], ids[-1], 1))

print("Empty seats: {}".format(set(ids).symmetric_difference(set(expected))))
