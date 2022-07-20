class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key



def inorder_tree_walk(x) -> None:
    if x != None:
        inorder_tree_walk(x.left)
        print(x.val)
        inorder_tree_walk(x.right)

root = Node(2)
root.right = Node(5)
root.right.right = Node(7)
root.right.right.right = Node(8)
root.right.right.left = Node(6)
root.right.right.left.left = Node(5)
inorder_tree_walk(root)