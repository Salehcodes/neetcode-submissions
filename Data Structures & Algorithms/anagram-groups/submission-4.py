class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hists = [[0]*26 for _ in range(len(strs))]
        d = {}
        for i,s in enumerate(strs):
            for c in s:
                hists[i][ord(c)-ord("a")]+=1
            key =tuple(hists[i])
            if key in d.keys():
                d[key].append(s)
            else:
                d[key]=[s]
        
        
        return list(d.values())