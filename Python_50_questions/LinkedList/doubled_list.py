class Node:

    def __init__(self, value):
        """
        In this case, we will only asign values on the beginning
        """
        self.value = value
        self.next = None
        self.prev = None
    
    def printNode(self):
        return "[[{}][   {}   ][{}]]".format(self.prev.value if self.prev else "x",self.value,self.next.value if self.next else "x")

class DoubledLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
    
    def create(self,arr):
        """
        Based of an array, we will create the doubled linked list
        """
        x = 0
        prev = None
        while x < len(arr):
            node = Node(arr[x])
            if x == 0:
                self.head = node
            else:
                prev.next = node
                node.prev = prev
            prev = node
            x += 1
        self.count = x
        return True
    
    def printList(self):
        pointer = self.head
        result = ""
        while pointer:
            result += pointer.printNode()
            pointer = pointer.next
        return result
    
    def printSize(self):
        return self.count
    
    def insert(self, value, pos):
        node = Node(value)
        if pos <= self.count:
            pointer = self.head
            prev = None
            x = 0
            while x < pos:
                prev = pointer
                pointer = pointer.next
                x += 1
            if pointer:
                pointer.prev = node
            node.next = pointer
            if x == 0:
                self.head = node
            else:
                prev.next = node
                node.prev = prev   
            self.count += 1
        return True
    
    def delete(self, index):
        if index < self.count:
            x = 0
            pointer = self.head
            prev = None
            next = pointer.next
            while x < index:
                prev = pointer
                pointer = pointer.next
                next = pointer.next
                x += 1
            if next:
                next.prev = prev
            if x == 0:
                self.head = next
            else:
                prev.next = next
            pointer = None
            self.count -= 1
        return True
            


if __name__ == "__main__":
    d = DoubledLinkedList()
    d.create([2,4,9,11,16])
    print("List of {} size -> {} ".format(d.printSize(),d.printList()))
    d.insert(7,2) #2,4,7,9,11,16
    print("List of {} size -> {} ".format(d.printSize(),d.printList()))
    d.insert(1,0) #1,2,4,7,9,11,16
    print("List of {} size -> {} ".format(d.printSize(),d.printList()))
    d.insert(13,6) #1,2,4,7,9,11,13,16
    print("List of {} size -> {} ".format(d.printSize(),d.printList()))
    d.insert(17,9) #1,2,4,7,9,11,13,16 (8 is invalid)
    print("List of {} size -> {} ".format(d.printSize(),d.printList()))
    d.insert(17,8) #1,2,4,7,9,11,13,16,17
    print("List of {} size -> {} ".format(d.printSize(),d.printList()))
    d.delete(2) #1,2,7,9,11,13,16,17
    print("List of {} size -> {} ".format(d.printSize(),d.printList()))
    d.delete(4) #1,2,7,9,13,16,17
    print("List of {} size -> {} ".format(d.printSize(),d.printList()))
    d.delete(0) #2,7,9,13,16,17
    print("List of {} size -> {} ".format(d.printSize(),d.printList()))
    d.delete(6) #2,7,9,13,16,17 #invalid position
    print("List of {} size -> {} ".format(d.printSize(),d.printList()))
    d.delete(5) #2,7,9,13,16
    print("List of {} size -> {} ".format(d.printSize(),d.printList()))

