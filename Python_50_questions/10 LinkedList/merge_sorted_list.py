"""
Merge two sorted linked lists and return it as a new sorted list. 
The new list should be made by splicing together the nodes of the first two lists.
"""
from single_list import Node

def mergeTwoLists(l1, l2):
    newList = Node(0,None)
    pos = newList
    while (l1 and l2):
        if l1.value < l2.value:
            pos.next = l1
            pos = pos.next
            l1 = l1.next
        else:
            pos.next = l2
            pos = pos.next
            l2 = l2.next
    while l1:
        pos.next = l1
        pos = pos.next
        l1 = l1.next
    while l2:
        pos.next = l2
        pos = pos.next
        l2 = l2.next
    return newList.next #Not neccesary to use first node with "0"

if __name__ == '__main__':
    n = Node (7, None)
    m = Node (5, n)
    c = Node (4, m)
    b = Node (3, c)
    a = Node (1, b)
    f = Node (6, None)
    e = Node (4, f)
    d = Node (2, e)
    newlist = mergeTwoLists(a, d)
    x= newlist
    while x:
        print(x.value)
        x = x.next
