class Node (object):
    def __init__(self, value) -> None:
        self.val = value
        self.left = None
        self.right = None


class binary_search_tree(object):
    def print_preorder(self, root):
        if not root:
            return []
        return [root.val] + self.print_preorder(root.left) + self.print_preorder(root.right)

    def print_inorder(self, root):
        if not root:
            return []
        return self.print_inorder(root.left) + [root.val] + self.print_inorder(root.right)

    def print_postorder(self, root):
        if not root:
            return []
        return self.print_inorder(root.left) + self.print_inorder(root.right) + [root.val]

    def init_path(self, root):
        res = []
        path = []
        pathlen = 0
        self.got_path(res, root, path, pathlen)
        return res

    def got_path(self, res, root, path, pathlen):
        if not root:
            return
        if len(path) > pathlen:
            path[pathlen] = root.val
        else:
            path.append(root.val)
        pathlen += 1
        if not root.left and not root.right:
            res.append(path[:pathlen])
        else:
            self.got_path(res, root.left, path, pathlen)
            self.got_path(res, root.right, path, pathlen)
        return res

    def got_path_2(self, root, current, res):
        if not root:
            return
        current.append(root.val)
        if not root.left and not root.right:
            res.append(current[:])
        self.got_path_2(root.left, current, res)
        self.got_path_2(root.right, current, res)
        current.pop()

    def find_sum(self, root, target):
        if not root:
            return
        target -= root.val
        if not root.left and not root.right and target == 0:
            return True
        return self.find_sum(root.left, target) or self.find_sum(root.right, target)

    def insert(self, root, value):
        if not root:
            return Node(value)
        elif value == root.val:
            pass
        elif value < root.val:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)
        return root

    def create(self, seq):
        root = None
        for word in seq:
            root = self.insert(root, word)
        return root

    def maxdepth(self, root):
        if not root:
            return 0
        return max(self.maxdepth(root.left), self.maxdepth(root.right)) + 1


tree = binary_search_tree()
root = tree.create([5, 4, 8, 11, 13, 4, 7, 2, 5, 1])

res = []
tree.got_path_2(root, [], res)
print(tree.maxdepth(root))
print(res)
