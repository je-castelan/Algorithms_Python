"""
Given the head of a linked list, remove the nth node from the end of the list and return its head
"""

from single_list import Node

def removeNthFromEndv1(head, n):
    """
    Runtime: 20 ms, faster than 70.61% of Python online submissions for Remove Nth Node From End of List.
    Memory Usage: 13.4 MB, less than 38.60% of Python online submissions for Remove Nth Node From End of List.
    """
    initial = head
    x = 0
    ending = head
    while x < n:
        ending = ending.next
        x += 1
    if not ending:
        return head.next
    while ending.next:
        initial = initial.next
        ending = ending.next
    initial.next = initial.next.next
    return head


def removeNthFromEndv2(head, n):
    """
    Runtime: 12 ms, faster than 98.96% of Python online submissions for Remove Nth Node From End of List.
    Memory Usage: 13.4 MB, less than 38.60% of Python online submissions for Remove Nth Node From End of List.
    """
    x = __getPosition(head)
    pointer = head
    if x == n:
        return head.next
    while x > n+1:
        pointer = pointer.next
        x -= 1
    pointer.next = pointer.next.next
    return head

def __getPosition(node):
    if not node.next:
        return 1
    return  __getPosition(node.next) + 1



if __name__ == "__main__":
    e = Node(5, None)
    d = Node(4, e)
    c = Node(3, d)
    b = Node(2, c)
    a = Node(1, b)

    l1 = removeNthFromEndv1(a,2)
    print("Removed to 2nd element from end in version 1 is {}".format(l1.printList()))

    e = Node(5, None)
    d = Node(4, e)
    c = Node(3, d)
    b = Node(2, c)
    a = Node(1, b)
    l1 = removeNthFromEndv2(a,2)
    print("Removed to 2nd element from end in version 2 is {}".format(l1.printList()))

    e = Node(5, None)
    d = Node(4, e)
    l1 = removeNthFromEndv1(d,1)
    print("Removed to 1st element from end in version 1 is {}".format(l1.printList()))

    e = Node(5, None)
    d = Node(4, e)
    l1 = removeNthFromEndv2(d,1)
    print("Removed to 1st element from end in version 2 is {}".format(l1.printList()))


    e = Node(5, None)
    d = Node(4, e)
    l1 = removeNthFromEndv1(d,2)
    print("Removed to 2nd element from end in version 1 is {}".format(l1.printList()))

    e = Node(5, None)
    d = Node(4, e)
    l1 = removeNthFromEndv2(d,2)
    print("Removed to 2nd element from end in version 2 is {}".format(l1.printList()))


    e = Node(5, None)
    l1 = removeNthFromEndv1(e,1)
    if not l1:
        print("List is empty")
    else:
        print("Removed to 1st element from end in version 1 is {}".format(l1.printList()))

    e = Node(5, None)
    l1 = removeNthFromEndv2(e,1)
    if not l1:
        print("List is empty")
    else:
       print("Removed to 1st element from end in version 2 is {}".format(l1.printList()))
   