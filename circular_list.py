from node import Node

class CircularList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def print_list(self):
        if self.is_empty():
            print("La lista esta vacia")
            return

        current = self.head
        while True:
            print(current.data, end="->")
            current = current.next
            if current == self.head:
                break
        print()

    def add_polinomio(self, coeficiente, grado):
        new_polinomio = Node(coeficiente, grado)
        if self.is_empty():
            self.head = new_polinomio
            new_polinomio.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_polinomio
            new_polinomio.next = self.head

    def edit_polinomio(self, search_data, new_data):
        if self.is_empty():
            print("La lista esta vacia")
            return
        current = self.head
        while True:
            if current.data == search_data:
                current.data = new_data
                return
            current = current.next
            if current == self.head:
                print(f"El elemento {search_data} no esta en la lista")
                return