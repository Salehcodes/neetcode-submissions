class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        freq = [[] for _ in range(len(nums)+1)]

        for kk,v in c.items():
            freq[v].append(kk)
        res=[]
        for i in range(len(freq)-1,-1,-1):
            for c in freq[i]:
                res.append(c)
                if len(res)==k:
                    return res