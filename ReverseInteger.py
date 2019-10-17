class Solution:
    def reverse(self, x: int) -> int:
        if x< 0:
            size=len(str(x))-1
        else:
            size=len(str(x))
       
        y=0
        if x < 0:
            isAbs=True
            x=abs(x)
        else:
            isAbs=False
        while size:
            size=size-1
            y=y*10+int(x%10)
            x=int(x/10)
        if isAbs:
            y=-1*y
        
        if y not in range(-pow(2, 31), pow(2, 31) - 1):
            return 0
        else:
            return y
        