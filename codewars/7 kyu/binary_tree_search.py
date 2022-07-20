# Given a number and a binary tree ( not a Binary Search Tree! ):
#
# return True/true if the given number is in the tree
# return False/false if it isn't
from __future__ import annotations
from typing import Optional


class Node:
    def __init__(self, value: int, left: Optional[Node] = None,
                 right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right

def iterative_search(x, k):

    while x is not None and k != x.value:
        if k > x.value:
            x = x.right
        else:
            x = x.left

    return x is not None

def recursive_search(x, k):
    """Recursive way"""
    if x is None:
        return 'There is no such number in the tree'
    if x is not None and k == x.value:
        return x
    if k > x.value:
        return recursive_search(x.right, k)
    else:
        return recursive_search(x.left, k)

root = Node(666, Node(555), Node(444))

# True and False
print(iterative_search(root, 666))
print(iterative_search(root, 333))
