class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        nums=candidates
        nums= sorted(nums)

        def bt(i,curr):
            if sum(curr)==target:
                res.append(curr[:])
                return
            if i>=len(nums) or sum(curr) > target:
                return
            
            curr.append(nums[i])
            bt(i+1,curr)
            curr.remove(nums[i])
            while(i+1 < len(nums) and nums[i+1]==nums[i]):
                i+=1
            bt(i+1,curr)
        
        bt(0,[])
        return res
