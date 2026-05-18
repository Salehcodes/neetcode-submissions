class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [0]*n
        if n<=3:
            return n
        arr[0]=1
        arr[1]=2
        arr[2]=3
        i=3
        while  i<=n-1:
            arr[i]=arr[i-1]+arr[i-2]
            i+=1

        return arr[n-1]