class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:


        def bt(i,res,curr):
            if sum(curr)==target:
                res.append(curr[:])
                return

            elif sum(curr) > target or i==len(nums):
                return
            else:
                curr.append(nums[i])
                bt(i,res,curr)
                curr.pop()
                bt(i+1,res,curr)
        res=[]
        bt(0,res,[])
        return res
