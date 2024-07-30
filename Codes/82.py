def breadth_first_traversal(root): 
    if root is None: 
        return

    queue = [] 
    queue.append(root) 

    while len(queue) > 0: 
        node = queue.pop(0)
        print(node.val, end=' ') 

        if node.left is not None: 
            queue.append(node.left) 

        if node.right is not None: 
            queue.append(node.right)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print("Breadth-first traversal:")
    breadth_first_traversal(root)
