head_movements = open("day9_input.txt").read().split("\n")

h = [0, 0]
points = {
    num: [0, 0]
    for num in range(1, 10)
}

first_past_positions = [(0, 0)]
last_past_positions = [(0, 0)]

play = {
    "R": lambda p: [p[0] + 1, p[1]],
    "L": lambda p: [p[0] - 1, p[1]],
    "U": lambda p: [p[0], p[1] + 1],
    "D": lambda p: [p[0], p[1] - 1]
}


def touch(v1, v2):
    if v1[0] == v2[0] and abs(v1[1] - v2[1]) <= 1:
        return True
    if v1[1] == v2[1] and abs(v1[0] - v2[0]) <= 1:
        return True

    return False


def diag(v1, v2):
    if abs(v1[0] - v2[0]) == 1 and abs(v1[1] - v2[1]) == 1:
        return True
    return False


def move_one_num(previous, point):
    if not touch(previous, point) and not diag(previous, point):
        if previous[0] == point[0]:
            point[1] = previous[1] + 1 * ((previous[1] < point[1]) or -1)
        elif previous[1] == point[1]:
            point[0] = previous[0] + 1 * ((previous[0] < point[0]) or -1)
        else:
            point[0] = previous[0] + (abs(previous[0] - point[0]) - 1) * ((previous[0] < point[0]) or -1)
            point[1] = previous[1] + (abs(previous[1] - point[1]) - 1) * ((previous[1] < point[1]) or -1)


for mov in head_movements:
    direction, num = mov.split(" ")
    while (num := int(num) - 1) >= 0:
        h = play[direction](h)
        for n, p in points.items():
            if n == 1:
                prev = h
            else:
                prev = points[n - 1]
            move_one_num(prev, p)
        first_past_positions.append(tuple(points[1]))
        last_past_positions.append(tuple(points[9]))

# 5683
print(len(set(first_past_positions)))
print(len(set(last_past_positions)))
