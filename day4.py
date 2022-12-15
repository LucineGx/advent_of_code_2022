pairs_of_elves = open("day4_input.txt").read().split("\n")

num_assignment_to_reconsider = 0
overlapping_assignment = 0
for pair in pairs_of_elves:
    first, second = pair.split(",")
    first_range = range(int(first.split("-")[0]), int(first.split("-")[1]) + 1)
    second_range = range(int(second.split("-")[0]), int(second.split("-")[1]) + 1)
    if len([z for z in first_range if z not in second_range]) == 0:
        num_assignment_to_reconsider += 1
    elif len([z for z in second_range if z not in first_range]) == 0:
        num_assignment_to_reconsider += 1
    if len([z for z in first_range if z in second_range]):
        overlapping_assignment += 1

print(num_assignment_to_reconsider)
print(overlapping_assignment)