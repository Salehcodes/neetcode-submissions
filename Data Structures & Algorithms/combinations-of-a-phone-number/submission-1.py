class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic={}
        
        dic[2]=["a","b","c"]
        dic[3]=["d","e","f"]
        dic[4]=["g","h","i"]
        dic[5]=["j","k","l"]
        dic[6]=["m","n","o"]
        dic[7]=["p","q","r","s"]
        dic[8]=["t","u","v"]
        dic[9]=["w","x","y","z"]

        res =[]
        def bt(index,curr):
            if index == len(digits):
                res.append("".join(curr[:]))
                return
            if len(dic[int(digits[index])])==3:
                x=3
            else:
                x=4
            for i in range(x):
                curr.append(dic[int(digits[index])][i])
                bt(index+1,curr)
                curr.pop()
        if len(digits)==0:
            return []
        bt(0,[])
        return res
            