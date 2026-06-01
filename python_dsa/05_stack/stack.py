class stack:
    def __init__(self):
        self.s = [] #s = empty list 

    def length(self):
        return len(self.s)
    #two way treat stack - 1.append() 2.insert()-[at start]
    #insert in stack using append or reverse insertion method.
    #we use reverse insert from start
    #beacuse push or pop always works on last element but here we use reverse i.e., insertion from start
    #push at start
    
    def push(self, value):
        self.s.insert(0, value)
    #peek at start means at top
    def peek(self):   #watch top element of stack
        if len(self.s) == 0:
            raise Exception("Stack is empty")
        else:
            return self.s[0]
        
    def pop(self):   #deletion happens in its reverse order
        if len(self.s) == 0:
            raise Exception("Stack is empty")
        else:
            return self.s.pop(0)
        
stk = stack()
stk.push(10)
stk.push(20)
stk.push(30)

print(stk.pop())
print(stk.pop())
print(stk.pop())
