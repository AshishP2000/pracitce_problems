class Node:
    def __init__(self, data=None):
        self.data = data
        self.nref = None
        self.pref = None


class DoubleLinkedList:

    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data," ",end="")
                n = n.nref

    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node


double = DoubleLinkedList()
double.add_begin(12)
double.add_begin(2)
double.print_ll()