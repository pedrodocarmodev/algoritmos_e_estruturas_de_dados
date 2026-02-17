class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.list_size = 0

    def insert_at_beginning(self, value):
        node = Node(value=value)

        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

        self.list_size += 1

    def insert_at_end(self, value):
        node = Node(value=value)
        if not self.tail:
            self.head = node
            self.tail = node
            self.list_size += 1
            return
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        self.list_size += 1

    def delete(self, value):
        cur = self.head
        while cur:
            if cur.value == value:
                if cur.prev:
                    cur.prev.next = cur.next
                else:
                    self.head = cur.next

                if cur.next:
                    cur.next.prev = cur.prev
                else:
                    self.tail = cur.prev

                self.list_size -= 1
                return
            cur = cur.next

    def find(self, value):
        cur = self.head
        while cur:
            if cur.value == value:
                return True
            cur = cur.next
        return False
    
    def size(self):
        return self.list_size
    
    def to_list(self):
        return_list = []
        cur = self.head
        while cur:
            return_list.append(cur.value)
            cur = cur.next
        return return_list
    
    def to_reverse_list(self):
        reverse_list = []
        cur = self.tail
        while cur:
            reverse_list.append(cur.value)
            cur = cur.prev
        return reverse_list  


def run_tests():
    dll = DoublyLinkedList()

    print("Inserindo no final...")
    dll.insert_at_end(10)
    dll.insert_at_end(20)
    dll.insert_at_end(30)

    assert dll.head.value == 10
    assert dll.tail.value == 30
    assert dll.to_list() == [10, 20, 30]
    assert dll.to_reverse_list() == [30, 20, 10]

    print("Inserindo no começo...")
    dll.insert_at_beginning(5)

    assert dll.head.value == 5
    assert dll.tail.value == 30
    assert dll.to_list() == [5, 10, 20, 30]
    assert dll.to_reverse_list() == [30, 20, 10, 5]

    print("Testando size...")
    assert dll.size() == 4

    print("Testando find...")
    assert dll.find(20) == True
    assert dll.find(999) == False

    print("Removendo elemento do meio...")
    dll.delete(20)

    assert dll.to_list() == [5, 10, 30]
    assert dll.to_reverse_list() == [30, 10, 5]
    assert dll.head.value == 5
    assert dll.tail.value == 30

    print("Removendo head...")
    dll.delete(5)

    assert dll.head.value == 10
    assert dll.tail.value == 30
    assert dll.to_list() == [10, 30]
    assert dll.to_reverse_list() == [30, 10]

    print("Removendo tail...")
    dll.delete(30)

    assert dll.head.value == 10
    assert dll.tail.value == 10
    assert dll.to_list() == [10]
    assert dll.to_reverse_list() == [10]

    print("Removendo último elemento...")
    dll.delete(10)

    assert dll.head is None
    assert dll.tail is None
    assert dll.size() == 0
    assert dll.to_list() == []
    assert dll.to_reverse_list() == []

    print("Inserindo novamente após limpar...")
    dll.insert_at_end(100)
    dll.insert_at_beginning(50)

    assert dll.head.value == 50
    assert dll.tail.value == 100
    assert dll.to_list() == [50, 100]
    assert dll.to_reverse_list() == [100, 50]

    print("Todos os testes passaram!")


if __name__ == "__main__":
    run_tests()