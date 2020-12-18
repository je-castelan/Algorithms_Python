"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

EVEN = PARES
ODD = NONES
"""

from single_list import Node

def oddEvenList(head):
    """
    Runtime: 32 ms, faster than 71.53% of Python online submissions for Odd Even Linked List.
    Memory Usage: 17.1 MB, less than 13.79% of Python online submissions for Odd Even Linked List.
    """
    if not head:
        return None
    eveninit = head.next
    evenpointer = eveninit
    oddpointer = head
    while eveninit and evenpointer and oddpointer:
        oddpointer.next = evenpointer.next
        oddpointer = evenpointer.next if evenpointer.next else oddpointer
        if evenpointer and evenpointer.next:
            evenpointer.next = oddpointer.next
            evenpointer = evenpointer.next
        else:
            break
    oddpointer.next = eveninit
    return head

if __name__ == "__main__":
    e = Node("e", None)
    d = Node("d", e)
    c = Node("c", d)
    b = Node("b", c)
    a = Node("a", b)

    newlist = oddEvenList(a)
    print("Oreder list odd-even is {}".format(newlist.printList()))

    f = Node("f",None)
    e = Node("e", f)
    d = Node("d", e)
    c = Node("c", d)
    b = Node("b", c)
    a = Node("a", b)

    newlist = oddEvenList(a)
    print("Oreder list odd-even is {}".format(newlist.printList()))

