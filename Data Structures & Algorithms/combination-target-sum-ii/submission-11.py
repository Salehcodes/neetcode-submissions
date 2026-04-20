class Solution:
    def combinationSum2(self, candidates, target):
        res = set()
        candidates.sort()

        def generate_subsets(i, cur, total):
            if total == target:
                res.add(tuple(cur))
                return
            if total > target or i == len(candidates):
                return
            j=i
            while j+1 < len(candidates) and candidates[j]==candidates[j+1]:
                j=j+1
            cur.append(candidates[i])
            generate_subsets(i+ 1, cur, total + candidates[i])
            cur.pop()
            generate_subsets(j + 1, cur, total)
            

        generate_subsets(0, [], 0)
        return [list(combination) for combination in res]