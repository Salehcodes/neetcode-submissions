class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        if len(s)==2:
            return s if s[0]==s[1] else s[0]
        maxp=1
        maxindex =[0,0]
        for i in range(len(s)-1):
            

            #odd
            if i!=0 and s[i+1]==s[i-1]:
                start=i
                r=i+2
                l=i-2
                current=3
                while l >=0 and r < len(s) and s[r]==s[l]:
                    l-=1
                    r+=1
                    current+=2
                if current > maxp:
                    maxindex = [l+1,r-1]
                maxp =max(current,maxp)
            
            #even
            if s[i+1]==s[i]:
                start =i
                r = i+2
                l = i-1
                current=2
                while l >=0 and r < len(s) and s[r]==s[l]:
                    l-=1
                    r+=1
                    current+=2
                if current > maxp:
                    maxindex = [l+1,r-1]
                maxp =max(current,maxp)
            
        return s[maxindex[0]:maxindex[1]+1]

        

        

    