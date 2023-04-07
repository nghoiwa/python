class Node:
    def __init__(self, value=0, next=None) -> None:
        self.val = value
        self.next = next
        return


def print_full_lsit(root):
    while root:
        print(root.val)
        root = root.next

def swap(root):
    head = root
    counter = 1
    while root.next:
        if counter%2 == 1:
            tmp = root.next
            root.next = tmp.next
            tmp.next = root
        root = root.next
        counter += 1
    return head

head = Node(4)
head.next = Node(2)
head.next.next = Node(1)
head.next.next.next = Node(3)
tmp = swap(head)
print_full_lsit(tmp)
