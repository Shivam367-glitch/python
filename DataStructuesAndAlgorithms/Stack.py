class Stack:
    def __init__(self):
        self.stack=[]
      #add element in stack  
    def push(self,a):
        self.stack.append(a)
    #remove element from stack
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is Empty")
        return self.stack.pop()
    # check if stack is empty
    def is_empty(self):
        return len(self.stack)==0
    #to get peek element from stack
    def peek(self):
        # if stack is empty then noo peek element is present ..
        if self.is_empty():
            raise Exception("Stack is Empty")
        return self.stack[-1]
    
    # size of the stack
    def size(self):
        return len(self.stack)
    
    def print(self):
        for i in range(len(self.stack)):
            print(self.stack[i],end=" ")
        print()
            
    
    
if __name__=="__main__":
    stack=Stack()
    for i in range(5):
        stack.push(i)
    print("elements  in stack :")
    stack.print()
    print("Top element in stack:")
    print(stack.peek())
    stack.pop()
    print("After poping from stack :")
    stack.print()
    
    
    
    