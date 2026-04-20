class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        def bt(openn,closen,res,curr):
            if openn==closen==n:
                res.append(curr[:])
                return
            if openn < n:
                curr.append("(")
                bt(openn+1,closen,res,curr)
                curr.pop()
            if openn > closen:
                curr.append(")")
                bt(openn,closen+1,res,curr)
                curr.pop()
        res=[]
        bt(0,0,res,[])
        print(res)
        return ["".join(lst) for lst in res ]
        