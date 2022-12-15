all_rucksacks = open("day3_input.txt").read().split("\n")


def get_item_prio(item: str) -> int:
    if 'a' <= item <= 'z':
        return ord(item) - 96
    if 'A' <= item <= 'Z':
        return ord(item) - 38
    else:
        breakpoint()


prio_score = 0
for rucksack in all_rucksacks:
    nb_items = len(rucksack) // 2
    first, second = rucksack[:nb_items], rucksack[nb_items:]
    wrong_item = [item for item in first if item in second][0]
    prio_score += get_item_prio(wrong_item)

print(prio_score)

prio_score = 0
i = 0
while i < len(all_rucksacks):
    common_item = [
        item
        for item in all_rucksacks[i]
        if item in all_rucksacks[i+1]
        and item in all_rucksacks[i+2]
    ][0]
    prio_score += get_item_prio(common_item)
    i += 3

print(prio_score)
