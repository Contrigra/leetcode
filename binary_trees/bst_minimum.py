from __future__ import annotations
from typing import Optional


class Node:
    def __init__(self, value: int, left: Optional[Node] = None,
                 right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right

def find_minumum(x):
    while x.left is not None:
        x = x.left

    return x, x.value



root = Node(666, Node(444), Node(555))

print(find_minumum(root))