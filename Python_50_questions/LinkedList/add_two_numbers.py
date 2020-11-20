"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

from single_list import Node

def addTwoNumbers(l1, l2):
    res = Node(0, None)
    pointer = res
    acum = 0
    while (l1 or l2) or acum > 0:
        suma = (l1.value if l1 else 0) + (l2.value if l2 else 0) + acum
        acum = suma // 10
        pointer.value = suma % 10
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        if l1 or l2 or acum:
            pointer.next = Node(0,None)
            pointer = pointer.next
    return res

if __name__ == '__main__':
    a3 = Node(3, None)
    a2 = Node(4, a3)
    a1 = Node(2, a2)

    b3 = Node(4, None)
    b2 = Node(6, b3)
    b1 = Node(5, b2)

    c = addTwoNumbers(a1, b1)

    print ("Sum of {} and {} is {}".format(a1.printList(), b1.printList(), c.printList()))

    b3 = Node(8, None)
    b2 = Node(6, b3)
    b1 = Node(5, b2)

    c = addTwoNumbers(a1, b1)

    print ("Sum of {} and {} is {}".format(a1.printList(), b1.printList(), c.printList()))



