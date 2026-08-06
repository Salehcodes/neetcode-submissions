class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        s = str(x)
        l = 0
        r =len(s)-1
        count=0
        if x < 0:
            return False
        while  l<=r and l<len(s) and s[l]==s[r]:
            if l==r:
                count+=1
            else:
                count+=2
            l+=1
            r-=1
        print(count)
        return count==len(s)