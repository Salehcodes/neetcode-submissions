class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def palindrome(string):
            l=0
            r=len(string)-1
            while l<r:
                if string[r]!=string[l]:
                    return False
                l+=1
                r-=1
            
            return True
        
        res =[]
        def bt(index,curr,strings):
            if curr[-1]==len(s):
                if strings not in res:
                    res.append(strings[:])
                return
            if index >=len(s):
                return
            
            if palindrome(s[curr[-1]:index+1]):
                strings.append(s[curr[-1]:index+1])
                curr.append(index+1)
                bt(index+1,curr,strings)
                curr.pop()
                strings.pop()
            bt(index+1,curr,strings)

      
        bt(0,[0],[])
        return res

            

            



        