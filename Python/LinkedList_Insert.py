from typing import Optional

class Node:
    def __init__(self, data):
        self.data = data
        self.next: Optional["Node"] = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
    def delete_At_Last(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next is not None and temp.next.next is not None:
            temp = temp.next
        temp.next = None
    def delete_At_position(self,k):
        t=self.head
        if t and t.data==k:
            self.head=t.next
            return
        prev: Optional[Node] = None
        while t and t.data!=k:
            prev=t
            t=t.next
        if t is None or prev is None:
            return
        prev.next=t.next


ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.delete_At_Last()
ll.insert(30)
ll.delete_At_position(2)
ll.display()