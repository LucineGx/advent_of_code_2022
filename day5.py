lines = open("day5_input.txt").read().split("\n")

ship = {0: []}
i = 0
while lines[i] != "":
    ship[i+1] = lines[i].split("-")
    i += 1

saved_ship = {key: value.copy() for key, value in ship.items()}

procedure = lines[10:]
while len(procedure):
    move = procedure.pop(0)
    move = move.replace("move ", "").replace(" from ", "-").replace(" to ", "-")
    amount, from_stack, to_stack = [int(n) for n in move.split("-")]
    while (amount := amount-1) >= 0:
        ship[to_stack].append(ship[from_stack].pop(-1))

del ship[0]
crates = "".join([stack[-1] for n, stack in ship.items()])
print(crates)

ship = saved_ship
procedure = lines[10:]
while len(procedure):
    move = procedure.pop(0)
    move = move.replace("move ", "").replace(" from ", "-").replace(" to ", "-")
    amount, from_stack, to_stack = [int(n) for n in move.split("-")]
    moving = []
    while (amount := amount-1) >= 0:
        moving.append(ship[from_stack].pop(-1))
    while len(moving):
        ship[to_stack].append(moving.pop(-1))

del ship[0]
crates = "".join([stack[-1] for n, stack in ship.items()])
print(crates)
