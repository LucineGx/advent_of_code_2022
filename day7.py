lines = open("day7_input.txt").read().split("\n")


tree = {"/": (None, 0, {})}
pwd = tree["/"]
for line in lines:
    if line.startswith("$ "):
        if line[2:4] == "cd":
            if line[5:] == "/":
                pwd = tree["/"]
            elif line[5:] == "..":
                pwd = pwd[0]
            else:
                pwd = pwd[2][line[5:]]

    else:
        if line.startswith("dir "):
            pwd[2][line[4:]] = pwd[2].get(line[4:], (pwd, 0, {}))

        else:
            weight, name = line.split(" ")
            pwd[2][name] = (None, int(weight), {})


response = {"score": 0, "folder_to_remove_size": 70000000}


def get_weight(_name, parent, _weight, content):
    result = 0
    if parent or _name == "/":
        for key, elem in content.items():
            result += get_weight(key, *elem)
        if result <= 100000:
            response["score"] += result
    else:
        result = _weight
    return result


outermost_size = get_weight("/", None, None, tree["/"][2])


print(f"sum of small folders = {response['score']}")
print(f"/ size: {outermost_size}")

excess_weight = 30000000 - (70000000 - outermost_size)
print(f"excess weight: {excess_weight}")


def get_smallest_removable_folder(_name, parent, _weight, content):
    result = 0
    if parent or _name == "/":
        for key, elem in content.items():
            result += get_smallest_removable_folder(key, *elem)
        if excess_weight < result < response["folder_to_remove_size"]:
            response["folder_to_remove_size"] = result
    else:
        result = _weight
    return result


get_smallest_removable_folder("/", None, None, tree["/"][2])

print(f"Size of the folder to remove: {response['folder_to_remove_size']}")
