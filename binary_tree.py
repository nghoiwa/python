class Node (object):
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
class binary_tree(object):
    def __init__(self, root) -> None:
        self.root = Node(root)
    def print_tree(self, print_method):
        if print_method == "preorder":
            return print(self.print_preorder(tree.root, ""))
        if print_method == "inorder":
            return print(self.print_inorder(tree.root, ""))
        else:
            return False
    def print_preorder(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-") 
            traversal = self.print_preorder(start.left, traversal)
            traversal = self.print_preorder(start.right, traversal)
        return traversal
    def print_inorder(self, start, traversal):
        if start:
            traversal = self.print_inorder(start.left, traversal)
            traversal += (str(start.value) + "-") 
            traversal = self.print_inorder(start.right, traversal)
        return traversal
##          1
##      2       3
##   4     5
tree = binary_tree (1)
tree.root.left = Node(2)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right = Node(3)
tree.root.right.left = Node(6)
tree.print_tree("inorder")
