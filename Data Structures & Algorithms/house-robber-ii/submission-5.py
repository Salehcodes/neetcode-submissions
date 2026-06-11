class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[1],nums[0])
                
        def helper(arr):
            dp=[0]*len(arr)
            dp[0]=arr[0]
            dp[1]=max(arr[1],arr[0])
            for i in range(2,len(arr)):
                dp[i]=max(dp[i-2]+arr[i],dp[i-1])
            print(dp)
            return dp[-1]

        return max(helper(nums[1:]),helper(nums[:-1]))
        

            