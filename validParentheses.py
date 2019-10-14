class Solution:
    
    def isValid(self, s: str) -> bool:
        items=[ ]
        top=''
        temp=''
        openBrac=False
        if s == '':
            return True
        
        for brac in s:
            print(brac)
            if not items:
                if brac == ')' or brac == '}' or brac == ']':
                    return False
                else:
                    items.append(brac)
                    top=items[-1]
                    print('At top '+top)
            elif brac == '(' or brac == '{' or brac == '[':
                items.append(brac)
                top=items[-1]
            elif brac == ')':
                if top == '(':
                    temp=items.pop()
                    if not items:
                        top=temp
                    else:
                        top=items[-1]    
                else:
                    return False
            elif brac == '}':
                if top == '{':
                    temp=items.pop()
                    if not items:
                        top=temp
                    else:
                        top=items[-1]   
                else:
                    return False
            elif brac == ']':
                if top == '[':
                    temp=items.pop()
                    if not items:
                        top=temp
                    else:
                        top=items[-1]   
                else:
                    return False
        if not items:
            return True
            
                    
                