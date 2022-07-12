class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add(self, data):
        new_node = Node(data)
        if self.__head is None:
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def insert(self, data, data_before):
        new_node = Node(data)
        if self.__head is None:
            self.__head = self.__tail = new_node
        else:
            node_before = self.find_node(data_before)
            if node_before is not None:
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if node_before == self.__tail:
                    self.__tail = new_node
            else:
                print("Node not found")

    def display(self):
        temp = self.__head
        while temp is not None:
            print(temp.get_data())
            temp = temp.get_next()

    def find_node(self, data):
        temp = self.__head
        while temp is not None:
            if temp.get_data() == data:
                return temp
            temp = temp.get_next()
        return None

    def delete(self, data):
        if self.__head is None:
            print("List is empty")
        else:
            node = self.find_node(data)
            if node is None:
                print("Node not found")
            elif node == self.__head:
                self.__head = self.__head.get_next()
                node.set_next(None)
                if node == self.__tail:
                    self.__tail = None
            else:
                node_before = None
                temp = self.__head
                while temp is not None:
                    if temp.get_next() == node:
                        node_before = temp
                        break
                    temp = temp.get_next()
                node_before.set_next(node.get_next())
                if node == self.__tail:
                    self.__tail = node_before
                node.set_next(None)


linked_list = LinkedList()
linked_list.add("Jose")
linked_list.add("Steve")
linked_list.add("Rebecca")
print("Initial Linked list:")
linked_list.display()

print("Linked list after adding Edwin:")
linked_list.add("Edwin")
linked_list.display()

print("Searching for a node in Linked list")
if linked_list.find_node("Rebecca") is not None:
    print("Node found")
else:
    print("Node not found")

print("Inserting Alex after Steve")
linked_list.insert("Alex", "Steve")
linked_list.display()

print("Linked list after deleting Rebecca")
linked_list.delete("Rebecca")
linked_list.display()
