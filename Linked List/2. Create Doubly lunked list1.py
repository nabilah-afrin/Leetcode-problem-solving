class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
class Doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append_begining(self,data):
        new_node = Node(data)
        # ll is empty
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
    def append_last(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
                  
    def append_position(self,data, position):
        
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
        
    def display(self):
        current = self.head
        while current:
            print(current.prev, "", current.data, "", current.next)
            current = current.next
        print("None")
    def delete_beginnig(self, data):
        
    def delete_mid(self, data, position):
    def delete_end(self,data):

        