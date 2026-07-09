class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hist1=[0 for _ in range(ord('z')-ord('a')+1)]
        hist2=[0 for _ in range(ord('z')-ord('a')+1)]

        for c in s:
            hist1[ord(c)-ord('a')]+=1
        for cc in t:
            hist2[ord(cc)-ord('a')]+=1
        
        return hist1 == hist2
