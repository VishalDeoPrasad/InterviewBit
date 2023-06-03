class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class Tree:
    def insert (self,node,value):
        if node is None:
            return Node(value)
        if value < node.data:
            node.left = self.insert(node.left, value)
        else:
            node.right = self.insert(node.right, value)
        return node
    
    def traverse_Inorder(self,root):
        if root is not None:
            self.traverse_Inorder(root.left)
            print(root.data, end=" ")
            self.traverse_Inorder(root.right)

tree = Tree()
root = Node(5)
tree.insert(root, 2)
tree.insert(root, 10)
tree.insert(root, 7)
tree.insert(root, 15)
tree.insert(root, 12)
tree.insert(root, 20)
tree.insert(root, 30)
tree.insert(root, 6)
tree.insert(root, 8)
print('Inorder--->', end=" ")
tree.traverse_Inorder(root)
