class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def islegal(curr):
            stck = []
            for i in range(len(curr)):
                if curr[i]==")" and len(stck)>0 and stck[-1] =="(":
                    stck.pop()
                else:
                    stck.append(curr[i])

            return len(stck)==0



        def bt(res,curr):
            if len(curr)==2*n:
                if islegal(curr):
                    res.append(curr[:])
                return
            
            curr.append("(")
            bt(res,curr)
            curr.pop()
            curr.append(")")
            bt(res,curr)
            curr.pop()
        res=[]
        bt(res,[])
        print(res)
        return ["".join(lst) for lst in res ]
        