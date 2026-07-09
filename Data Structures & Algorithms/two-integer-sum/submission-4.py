class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,num in enumerate(nums):
            d[num]=i
        
        for i,num in enumerate(nums):
            tosearch = target-num
            if tosearch in d.keys():
                index = d[tosearch]
                if index !=i:
                    return [i,d[tosearch]]
        

