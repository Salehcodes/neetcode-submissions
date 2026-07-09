class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = defaultdict(int)
        for num in nums:
            d[num] +=1
        
        for num in nums:
            if d[num] >1:
                return True
        
        return False

        