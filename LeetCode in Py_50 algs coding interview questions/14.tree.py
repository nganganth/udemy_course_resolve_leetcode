# a Tree must be: connected; acyclic; undirectional

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value
    
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data)
        inorder(node.right)

def preorder(node):
    if node is not None:
        print(node.data)
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data)

root = Node(4)
root.left = Node(5)
root.right = Node(6)

root.left.left = Node(7)
root.right.right = Node(8)

# inorder traversal: left - root - right
print("inorder traversal")
inorder(root)

# preorder traversal: root - left - right
print("preorder traversal")
preorder(root)

# postorder traversal: left - right - root
print("postorder traversal")
postorder(root)
