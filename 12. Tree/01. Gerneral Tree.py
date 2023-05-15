class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, data):
        self.parent = self
        self.children.append(data)

    def get_level(self):
        level = 0
        temp = self.parent
        while temp:
            level += 1
            temp = temp.parent
        return level

    def print_tree(self):
        spaces = ' '*self.get_level()*1
        print(spaces + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

laptop = TreeNode("Laptop")
laptop.add_child(TreeNode("Mac"))
laptop.add_child(TreeNode("Microsoft"))
laptop.add_child(TreeNode("Thinkpad"))

cellphone = TreeNode("Cell Phone")
cellphone.add_child(TreeNode("iPhone"))
cellphone.add_child(TreeNode("Google Pixel"))
cellphone.add_child(TreeNode("Vivo"))

tv = TreeNode("TV")
tv.add_child(TreeNode("Samsung"))
tv.add_child(TreeNode("LG"))

root = TreeNode("Electronic")
root.add_child(laptop)
root.add_child(cellphone)
root.add_child(tv)

print(root)
root.print_tree()

