# will have no null value
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class CircularLL:
    def __init__(self):
        self.head = None
    def append(self,value):
        new_node = Node(value)       
        # for empty LL
        if not self.head:
            self.head = new_node
            new_node.next = self.head   #when we have only one node, circular will circle back to its own position

        # when list is not empty
        else:
            current = self.head
            while current.next!= self.head: #confirming there are mutiple nodes
                current = current.next #move until reach the last point
            current.next = new_node
            new_node.next =self.head
                
        
    def display(self):
        if not self.head:
            print("The Linked List is empty.")
        else:
            temp = self.head
            print(self.head)
            while True:
                print("-----------------")
                print(temp.data)
                print(temp.next)
                print("-----------------")

                temp = temp.next

                if temp == self.head:
                    break
circularLL = CircularLL()
circularLL.append(10)
circularLL.append(100)
circularLL.append(1000)
circularLL.display()
            