class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic={}
        ky=None
        
        for i in range(0,len(s)):
            if not dic.get(s[i]):
                dic[s[i]]=1
            else:
                dic[s[i]]=dic.get(s[i])+1
                
        for k in dic:
            if dic.get(k) == 1:
                ky=k
                break
        if ky:
            return s.index(ky)
        else:
            return -1
            