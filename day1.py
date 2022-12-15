input = open("day1_input.txt").read().split("\n")

elfs = []
i = 0

while i < len(input):
    new_elf = 0
    while i < len(input) and input[i] != "":
        new_elf += int(input[i])
        i += 1
    elfs.append(new_elf)
    i += 1

elfs = sorted(elfs, reverse=True)
top3 = elfs[0:3]
print(top3)
print(sum(top3))
