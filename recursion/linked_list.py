class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Make a string representation of linked list values

def stringify(node):
    if node is None:
        return 'None'
    else:
        return f'{node.data} -> {stringify(node.next)}'


print(stringify(Node(0, Node(1, Node(4, Node(9, Node(16)))))))
print(stringify(Node(0, Node(1, Node(2, Node(3))))))
print(stringify(None))
