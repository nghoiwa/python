class Node:
    def __init__(self, value=0, next=None) -> None:
        self.val = value
        self.next = next
        return


def mergesort(root):
    if not root or not root.next:
        return root
    left = root
    tmp = findmid(root)
    right = tmp.next
    tmp.next = None
    left_sort = mergesort(left)
    right_sort = mergesort(right)
    return merge(left_sort, right_sort)


def merge(left, right):
    dummy = Node(-1)
    prev = dummy
    while left and right:
        if left.val < right.val:
            prev.next = left
            left = left.next
        else:
            prev.next = right
            right = right.next
        prev = prev.next
    prev.next = left or right
    return dummy.next


def findmid(root):
    slow, fast = root, root
    fast = fast.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def print_full_lsit(root):
    while root:
        print(root.val)
        root = root.next

head = Node(4)
head.next = Node(2)
head.next.next = Node(1)
head.next.next.next = Node(3)
print_full_lsit(mergesort(head))
