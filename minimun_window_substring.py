class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic={}
        dic1={}
        left=0
        right=0
        temp=""
        final=""
        
        for i in range(0,len(t)):
            if not dic1:
                dic1[t[i]]=1
            elif not dic1.get(t[i]):
                dic1[t[i]]=1
            else:
                dic1[t[i]]=dic1.get(t[i]) + 1;
        #print(str(dic1)) 
        
        while right <= len(s):
            temp=s[left:right]
            print(temp)
            if not self.checkCount(temp,dic1):
                right+=1
            else:
                if final is "":
                    final = temp
                elif final is not "" and len(temp) <= len(final):
                     final=temp
                left+=1
        return final
                   
    def checkCount(self, temp:str, dic1) -> bool:
        flag=1
        dic={}
        print(temp)
        for keys in dic1:
            if temp.find(keys) != -1:
                if not dic:
                    dic[keys]=1
                elif not dic.get(keys):
                    dic[keys]=1
                else:
                    dic[keys]=dic.get(keys)+1
            else:
                return False
        
        for keys in dic1:
            if dic:
                if not dic.get(keys):
                    return False
                elif dic.get(keys) < dic1.get(keys):
                    return False
        return True
      