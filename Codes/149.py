class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def detectLoop(head):
    slow_p = head 
    fast_p = head 
    while slow_p and fast_p and fast_p.next:
        slow_p = slow_p.next
        fast_p = fast_p.next.next
        if slow_p == fast_p:
            return True
    return False

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print(detectLoop(head))

head.next.next.next.next.next = head.next

print(detectLoop(head))
