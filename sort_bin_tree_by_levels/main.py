def height(node):
    if not node:
        return 0
    else:
        left_n = height(node.left)
        right_n = height(node.right)

        return max(left_n + 1, right_n + 1)


def add_level(node, level):
    res = []
    if not node:
        return []
    if level == 1:
        return [node.value]
    elif level > 1:
        res.extend(add_level(node.left, level - 1))
        res.extend(add_level(node.right, level - 1))
    return res


def tree_by_levels(node):
    if not node:
        return []
    h, res = height(node), []
    for i in range(1, h + 1):
        res.extend(add_level(node, i))
    return res
