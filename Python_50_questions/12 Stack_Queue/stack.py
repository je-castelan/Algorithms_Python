class Stack:
    def __init__(self, size):
        self.size = size
        self.elements = []

    def push(self, value):
        if len(self.elements) == self.size:
            return False
        self.elements.append(value)
        return  True
    
    def top(self):
        if len(self.elements) == 0:
            return None
        return self.elements[-1]

    def pop(self):
        if len(self.elements) == 0:
            return False
        self.elements.pop()
        return True


if __name__ == "__main__":
    s = Stack(3)
    s.push("a")
    print(s.top())
    s.push("b")
    print(s.top())
    s.push("c")
    print(s.top())
    s.push("d")
    print(s.top())
    s.pop()
    print(s.top())
    s.push("d")
    print(s.top())
    s.pop()
    print(s.top())
    s.pop()
    print(s.top())
    s.pop()
    print(s.top())
    s.pop()
    print(s.top())