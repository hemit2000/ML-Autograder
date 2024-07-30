class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def findDepth(root):
    if root is None:
        return 0

    else:
        left_height = findDepth(root.left)
        right_height = findDepth(root.right)

        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1

# Create the binary tree
root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(5)
root.left.right = Node(15)

print(findDepth(root))
