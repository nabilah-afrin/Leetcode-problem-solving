class Node:
    def __init__(self, val = 0):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append_begin(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head # appending in the beginning of the list
            # make the new node as the new head of the list
            # update the head
            self.head = new_node
            
    def append_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current= current.next # move to the last node
            current.next = new_node
    
    def display(self):
        current = self.head
        while current:
            print(current.val , " " , current.next)
            current = current.next
    
    def search(self,data):
        current= self.head
        while current:
            if current.val == data:
                return True
            current = current.next
        return False
    
    def delete(self, data):
        current = self.head
        prev = None
        while current
            
        
        
l1 = LinkedList()
l1.append_begin(10)
l1.append_begin(15)
l1.append_begin(20)
l1.display()
print(l1.search(10))