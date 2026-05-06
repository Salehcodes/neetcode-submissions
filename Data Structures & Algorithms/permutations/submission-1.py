class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]


        def bt(curr):
            if len(curr)==len(nums):
                res.append(curr[:])
                return
            
            for i in range(len(nums)):
                if nums[i] not in curr:
                    curr.append(nums[i])
                    bt(curr)
                    curr.remove(nums[i])
        bt([])
        return res