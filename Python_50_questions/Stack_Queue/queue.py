class Queue:
    def __init__(self):
        self.values = []
    
    def enqueue(self, value):
        self.values.append(value)

    def front(self):
        return self.values[0] if len(self.values) > 0 else None
    
    def dequeue(self):
        value = None
        if len(self.values) > 0:
            value = self.values[0]
            self.values.pop(0)
        return value


if __name__ == "__main__":
    q = Queue()
    q.enqueue("a")
    print(q.front())
    q.enqueue("b")
    print(q.front())
    q.enqueue("c")
    print(q.front())
    q.dequeue()
    print(q.front())
    q.dequeue()
    print(q.front())
    q.enqueue("d")
    print(q.front())
    q.dequeue()
    print(q.front())
    q.dequeue()
    print(q.front())
    