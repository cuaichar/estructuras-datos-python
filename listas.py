# -*- coding: utf-8 -*-
# Parte C — Listas Enlazadas

# Nodo para lista simple
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# TODO 5: Lista enlazada simple
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # mantener tail permite insert_end en O(1)

    def insert_front(self, data):
        nuevo = Node(data)
        nuevo.next = self.head
        self.head = nuevo
        if self.tail is None:
            self.tail = nuevo

    def insert_end(self, data):
        nuevo = Node(data)
        if self.tail is None:
            self.head = self.tail = nuevo
        else:
            self.tail.next = nuevo
            self.tail = nuevo

    def traverse(self):
        actual = self.head
        elementos = []
        while actual:
            elementos.append(str(actual.data))
            actual = actual.next
        print(" -> ".join(elementos) if elementos else "Lista vacía")

# Nodo para lista doblemente enlazada
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# TODO 6: Lista doblemente enlazada
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # tail permite insert_end y traverse_backward en O(1) amortizado

    def insert_front(self, data):
        nuevo = DNode(data)
        if self.head is None:
            self.head = self.tail = nuevo
        else:
            nuevo.next = self.head
            self.head.prev = nuevo
            self.head = nuevo

    def insert_end(self, data):
        nuevo = DNode(data)
        if self.tail is None:
            self.head = self.tail = nuevo
        else:
            nuevo.prev = self.tail
            self.tail.next = nuevo
            self.tail = nuevo

    def traverse_forward(self):
        actual = self.head
        elementos = []
        while actual:
            elementos.append(str(actual.data))
            actual = actual.next
        print("Adelante: " + (" <-> ".join(elementos) if elementos else "vacía"))

    def traverse_backward(self):
        actual = self.tail
        elementos = []
        while actual:
            elementos.append(str(actual.data))
            actual = actual.prev
        print("Atrás:    " + (" <-> ".join(elementos) if elementos else "vacía"))

if __name__ == "__main__":
    print("== Listas Enlazadas ==")

    print("\nLista simple:")
    l = LinkedList()
    l.insert_front(10)
    l.insert_end(20)
    l.insert_front(5)
    l.insert_end(30)
    l.traverse()  # 5 -> 10 -> 20 -> 30

    print("\nLista doblemente enlazada:")
    dl = DoublyLinkedList()
    dl.insert_front(1)
    dl.insert_end(2)
    dl.insert_end(3)
    dl.insert_front(0)
    dl.traverse_forward()   # 0 <-> 1 <-> 2 <-> 3
    dl.traverse_backward()  # 3 <-> 2 <-> 1 <-> 0
