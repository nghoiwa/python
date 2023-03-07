class Node:
    def __init__(self, value=0, next=None) -> None:
        self.value = value
        self.next = next
        return

def print_list_element(head):
    return head.value

def print_full_list(head):
    if head != None:
        print(print_list_element(head))
        print_full_list(head.next)
    else:
        return

def reverse_link_list(head):
    # 1 -> 2 -> 3
    prev = None
    #prev 1 -> 2 -> 3
    while head:
        current = head
        # None 1 (head and current) -> 2 -> 3
        head = head.next
        # None 1 (current) 2 (head) -> 3
        current.next = prev
        # None <- 1 (current) 2 (head) -> 3
        prev = current
        # None <- 1 prev -> 2 (head) -> 3
    return prev

def reverse_link_list_recur(head, prev=None):
    if not head:
        return prev
    next = head.next
    head.next = prev
    return reverse_link_list_recur(next, head)
    """if not head or not head.next:
        return head
    current = reverse_link_list_recur(head.next)
    print(current.value)
    print("head " + str(head.value))
    head.next.next = head
    print("head.next.next " + str(head.next.next.value))
    head.next = None
    return current"""
def reverse(head, prev=None):
    while head:
        tmp = head
        head = head.next
        tmp.next = prev
        prev = tmp
    return prev

def reversetest(head):
    dummy = Node(None, head)
    prev, current = dummy ,head
    while current:
        tmp = current
        current = current.next
        tmp.next = prev
        prev = tmp
        

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
print_full_list(head)
print("---")
"""result = reverse_link_list(head)
print_full_list(result)"""
result3 = reverse(head)
print_full_list(result3)