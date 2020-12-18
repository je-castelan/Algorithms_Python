"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""
from single_list import Node

def hasCycle(head):
    slow = head
    faster = head
    while slow and faster and faster.next:
        slow = slow.next
        faster = faster.next.next if faster.next else None
        if slow == faster:
            return True
    return False

if __name__ == "__main__":
    n4 = Node(-4,None)
    n3 = Node(0,n4)
    n2 = Node(2,n3)
    n1 = Node(3,n2)
    print("Has cycle? {}".format(hasCycle(n1)))
    n4.next = n2 #loop
    print("Has cycle? {}".format(hasCycle(n1)))
    n5 = Node(6,None)
    print("Has cycle? {}".format(hasCycle(n5)))
    ne = Node(9,None)
    nd = Node(8, ne)
    nc = Node(11,nd)
    nb = Node(5,nc)
    na = Node(1,nb)
    print("Has cycle? {}".format(hasCycle(na)))
    ne.next = nb
    print("Has cycle? {}".format(hasCycle(na)))