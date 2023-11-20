# we know that every operation in stack is condcucted in O(1) times
# Stack Operations: 
# push(): Insert a new element into the stack i.e just insert a new element at the beginning of the linked list.
# pop(): Return the top element of the Stack i.e simply delete the first elemen from the linked list.
# peek(): Return the top element.
# display(): Print all elements in Stack.
# head is the first element of any linked list

#Output: [1,2,3]
class Node:
    def __init__(self,data) -> None:
        self.val = data
        self.next = None
class  Stack:
    def __init__(self):
        #introduce the head or ll
        self.head =None #because we are initializing the stack as impty
    
    # check if the stack is empty or not
    def is_empty(self):
        if self.head is None:
            return True
        else: return False
    
    def push(self,data): #we need to initialize the element under the function, rather than creating an object outside
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node #after creating the pointer we  get the whole stack 
        
    def pop(self):
        #if the stack is empty
        if self.head is None: return None
        popped_node = self.head
        # asiign the new head
        self.head = self.head.next
        return popped_node.data
    
    def peek(self):
        if self.head is None: return None
        print(self.head.data)
        
stack = Stack()

# Push some elements onto the stack
stack.push(1)
stack.push(2)
stack.push(3)

# Pop the elements off the stack
print(stack.pop())  # 3
print(stack.pop())  # 2
print(stack.pop())  # 1

