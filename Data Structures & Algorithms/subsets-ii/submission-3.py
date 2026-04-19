class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def bt(curr  , res,index):
            if index == len(nums):
                if curr not in res:
                    res.append(curr[:])
                return
            
            curr.append(nums[index])
            bt(curr,res,index+1)
            curr.remove(nums[index])
            bt(curr,res,index+1)
        
        nums.sort()
        bt([],res,0)
        return res