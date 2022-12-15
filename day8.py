import pandas as pd
tree_map = open("day8_input.txt").read().split("\n")


trees = pd.DataFrame([
    {"x": x, "y": y, "height": height, "visible": False}
    for y, tree_line in enumerate(tree_map)
    for x, height in enumerate(tree_line)
])


def get_visible_tree(line):
    return [
        max(line[0:i+1]) == height and line[0:i+1].count(height) == 1
        for i, height in enumerate(line)
    ]


for y in range(0, 99):
    # check left
    trees.loc[trees["y"] == y, "visible"] = (trees[trees["y"] == y]["visible"] | pd.Series(get_visible_tree(tree_map[y]), index=trees[trees["y"] == y].index))

    # check right
    trees.loc[trees["y"] == y, "visible"] = (trees[trees["y"] == y]["visible"] | pd.Series(get_visible_tree(tree_map[y][::-1]), index=trees[trees["y"] == y].index.to_list()[::-1]))

    x = y
    col = [l[x] for l in tree_map]
    # check up
    trees.loc[trees["x"] == x, "visible"] = (trees[trees["x"] == x]["visible"] | pd.Series(get_visible_tree(col), index=trees[trees["x"] == x].index))

    # check down
    trees.loc[trees["x"] == x, "visible"] = (trees[trees["x"] == x]["visible"] | pd.Series(get_visible_tree(col[::-1]), index=trees[trees["x"] == x].index.to_list()[::-1]))

print(trees["visible"].sum())

scenic_max = 0
max_row = None

for index, row in trees.iterrows():
    scenic_l = 1
    scenic_r = 0
    scenic_u = 0
    scenic_d = 0
    for x in range(row["x"] - 1, 0, -1):
        scenic_l += 1
        if tree_map[row["y"]][x] >= row["height"]:
            break
    for x in range(row["x"] + 1, 99):
        scenic_r += 1
        if tree_map[row["y"]][x] >= row["height"]:
            break
    for y in range(row["y"] - 1, 0, -1):
        scenic_u += 1
        if tree_map[y][row["x"]] >= row["height"]:
            break
    for y in range(row["y"] + 1, 99):
        scenic_d += 1
        if tree_map[y][row["x"]] >= row["height"]:
            break
    scenic = scenic_l * scenic_r * scenic_u * scenic_d
    scenic_max = max(scenic, scenic_max)
    if scenic == 563040:
        breakpoint()

print(scenic_max)
