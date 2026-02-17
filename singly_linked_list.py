class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def insert_at_end(self, value):
        node = Node(value)
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = node
        else:
            self.head = node

    def delete(self, value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        prev = self.head
        current = self.head.next

        while current:
            if current.value == value:
                prev.next = current.next
                return
            prev = current
            current = current.next

    def find(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def size(self):
        current = self.head
        size = 0
        while current:
            size += 1
            current = current.next
        return size
    
    def to_list(self):
        r_list = []
        current = self.head
        while current:
            r_list.append(current.value)
            current = current.next
        return r_list


def run_tests():
    ll = LinkedList()

    print("Inserindo no final...")
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    assert ll.to_list() == [10, 20, 30]

    print("Inserindo no começo...")
    ll.insert_at_beginning(5)
    assert ll.to_list() == [5, 10, 20, 30]

    print("Testando size...")
    assert ll.size() == 4

    print("Testando find...")
    assert ll.find(20) == True
    assert ll.find(99) == False

    print("Deletando elemento do meio...")
    ll.delete(20)
    assert ll.to_list() == [5, 10, 30]

    print("Deletando primeiro elemento...")
    ll.delete(5)
    assert ll.to_list() == [10, 30]

    print("Deletando último elemento...")
    ll.delete(30)
    assert ll.to_list() == [10]

    print("Deletando elemento inexistente...")
    ll.delete(999)
    assert ll.to_list() == [10]

    print("Todos os testes passaram!")

if __name__ == "__main__":
    run_tests()