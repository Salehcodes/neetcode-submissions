class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        curr = []
        def bt(curr,res):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            
            for i in range(len(nums)):
                if nums[i] in curr:
                    continue
                curr.append(nums[i])
                bt(curr,res)
                curr.remove(nums[i])
        bt(curr,res)
        return res