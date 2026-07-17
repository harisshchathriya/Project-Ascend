class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

    def find_middle(self):
        slow_ptr = self.head
        fast_ptr = self.head

        if self.head is not None:
            while fast_ptr is not None and fast_ptr.next is not None:
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next
            return slow_ptr.data


dll = DoublyLinkedList()
dll.insert(10)
dll.insert(20)
dll.insert(30)
print(dll.find_middle())