class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insert function (BST style insertion)
def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root


# Traversal functions
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# Print tree sideways
def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print_tree(root.right, level + 1, "R----")
        print("     " * level + prefix + str(root.data))
        print_tree(root.left, level + 1, "L----")


# Driver code
if __name__ == "__main__":
    root = None
    elements = ['D', 'B', 'A', 'C', 'F', 'E']  # Slightly rearranged for BST clarity

    for elem in elements:
        root = insert(root, elem)

    print("\nTree Structure:")
    print_tree(root)

    print("\nInorder Traversal:")
    inorder(root)
    print("\nPreorder Traversal:")
    preorder(root)
    print("\nPostorder Traversal:")
    postorder(root)
