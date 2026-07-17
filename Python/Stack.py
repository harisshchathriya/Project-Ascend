class stack:
    def __init__(self, data):
        self.items = []
        self.size=data
        self.top=-1
    def is_full(self):
        return self.top == self.size - 1
    def is_empty(self):
        return self.top==-1
    def push(self,data):
        if not self.is_full():
            self.items.append(data)
            self.top += 1
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
            self.top-=1
    def peek(self):
        return self.items[len(self.items) - 1]
    def display(self):
        for i in range(self.top, -1, -1):
            print(self.items[i], end=" ")
        print()
        print(self.is_full())
        print(self.is_empty())
        print(self.peek())
        print(self.push(10))
        print(self.pop())
d=int(input())
s=stack(d)
for i in range(d):
    a=int(input())
    s.push(a)
s.display()