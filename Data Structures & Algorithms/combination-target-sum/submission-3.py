class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]

        def bt(i,curr):
            if sum(curr)==target:
                res.append(curr[:])
                return
            if i==len(nums) or sum(curr)>target:
                return
            curr.append(nums[i])
            bt(i,curr)
            curr.remove(nums[i])
            bt(i+1,curr)
        
        bt(0,[])
        return res