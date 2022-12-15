rps_tournament = open("day2_input.txt").read().split("\n")

# rock = A
# paper = B
# scissors = C
# C > B > A > C
order = ["C", "B", "A"]
wrong_convert = {
    "X": "A",
    "Y": "B",
    "Z": "C",
}
shapes = {
    "A": 1,
    "B": 2,
    "C": 3,
}

WIN = 6
DRAW = 3
LOSE = 0
convert = {
    "X": LOSE,
    "Y": DRAW,
    "Z": WIN,
}


def wrong_play(_adv: str, _you: str) -> int:
    result = order.index(_adv) - order.index(_you)
    if result == 0:
        return DRAW
    if result % 3 == 1:
        return WIN
    if result % 3 == 2:
        return LOSE
    else:
        breakpoint()


score = 0
for round in rps_tournament:
    adv, you = round.split(" ")
    you = wrong_convert[you]
    score += wrong_play(adv, you)
    score += shapes[you]

print(f"wrong score: {score}")


def play(_adv: str, _result: int) -> str:
    if _result == DRAW:
        return _adv
    if _result == WIN:
        return order[(order.index(_adv) - 1) % 3]
    if _result == LOSE:
        return order[(order.index(_adv) + 1) % 3]
    else:
        breakpoint()


score = 0
for round in rps_tournament:
    adv, result = round.split(" ")
    result = convert[result]
    score += result
    score += shapes[play(adv, result)]

print(f"good score: {score}")

