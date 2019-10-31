class MinStack:
    stack=[]
    stack1=[]
    minV=None
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        global stack,stack1,minV
        stack=[]
        stack1=[]
        minV=None
        trav=True
        if stack:
            minV=stack[-1]
        
        
    def push(self, x: int) -> None:
        global minV
        stack.append(x)
        if minV == None:
            minV=stack[-1]
        if x < minV:
            minV=x
           
       

    def pop(self) -> None:
        global minV
        last=stack[-1]
        stack.pop()
        if minV == last and stack:
            minV=stack[-1]
        elif not stack:
            minV=None

    def top(self) -> int:
        if stack:
            return stack[-1]
        else:
            return -1
            

    def getMin(self) -> int:
        global stack,stack1,minV
        for i in range(0,len(stack)):
            if stack[i] <= minV:
                minV=stack[i]
            else:
                stack1.append(stack[i])
     
        stack1=[]
        return minV    
    

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()