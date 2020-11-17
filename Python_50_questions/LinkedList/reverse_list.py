"""
Reverse a singly linked list.
"""

from single_list import Node


def reverseList(head):
    pointer = head
    prev = None
    while pointer:
        nextpointer = pointer.next
        pointer.next = prev
        prev = pointer
        pointer = nextpointer
    return prev


def printList(mylist):
    result = ""
    while mylist:
        result +=  "{} -> ".format(mylist.value)
        mylist = mylist.next
    return result

if __name__ == "__main__":
    e = Node("e", None)
    print("Reverse of [{}] is [{}]".format(printList(e),printList(reverseList(e))))
    d = Node("d", e)
    c = Node("c", d)
    b = Node("b", c)
    a = Node("a", b)
    print("Reverse of [{}] is [{}]".format(printList(a),printList(reverseList(a))))
    
