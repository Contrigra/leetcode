class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def tree_search(x, k):
    if x is None or k == x.val:
        return x
    if k < x.val:
        return tree_search(x.left, k)
    else:
        return tree_search(x.right, k)


