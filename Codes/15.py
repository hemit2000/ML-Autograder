class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
   
    def pop(self):
        if len(self.items) == 0: 
            return None
        else: 
            return self.items.pop()
    
    def peek(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items[-1]

stack=Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.peek())

