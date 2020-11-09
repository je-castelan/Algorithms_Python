
class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class SingleLinkedList:
    def __init__(self, head):
        self.head = head
    
    def displayList(self):
        pointer = self.head
        listing = "{}".format(pointer.value)
        while pointer.next:
            pointer = pointer.next
            listing += " {}".format(pointer.value)
        return listing
    
    def insert(self, value, position):
        x = 0
        pointer = self.head
        prev = None
        while x < position:
            x += 1
            prev = pointer
            pointer = pointer.next
            if not pointer:
                break
        node = Node(value, pointer)
        
        if x == 0:
            self.head = node
        else:
            prev.next = node
        return True

    def delete(self, key):
        isHeader = True
        pointer = self.head
        while pointer.value != key:
            prev = pointer
            pointer = pointer.next
            if not pointer:
                return False
            isHeader = False
        if isHeader:
            self.head = pointer.next
        else:
            prev.next = pointer.next
        pointer = None
        return True

if __name__ == "__main__":
    d = Node (9,None)
    c = Node (7, d)
    b = Node (5, c)
    a = Node (3, b)
    s = SingleLinkedList(a)
    print("List has values [{}]".format(s.displayList()))
    s.insert(6,2)
    print("List has values [{}]".format(s.displayList()))
    s.insert(10,5)
    print("List has values [{}]".format(s.displayList()))
    s.insert(2,0)
    print("List has values [{}]".format(s.displayList()))
    s.insert(1,0)
    print("List has values [{}]".format(s.displayList()))
    s.delete(6)
    print("List has values [{}]".format(s.displayList()))
    s.delete(9)
    print("List has values [{}]".format(s.displayList()))
    s.delete(11)
    print("List has values [{}]".format(s.displayList()))
    s.delete(1)
    print("List has values [{}]".format(s.displayList()))
    s.delete(2)
    print("List has values [{}]".format(s.displayList()))
    s.delete(1)
    print("List has values [{}]".format(s.displayList()))