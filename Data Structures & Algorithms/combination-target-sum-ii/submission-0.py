class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        result = []

        def dfs(pos, curr, target):
            if target == 0:
                result.append(curr.copy())
                return 
            if target < 0 or pos >= len(candidates):
                return 

            prev = -1
            for i in range(pos, len(candidates)):
                if prev == candidates[i]:
                    continue
                curr.append(candidates[i])
                dfs(i + 1, curr, target - candidates[i])

                curr.pop()
                prev = candidates[i]
            return result
        
        dfs(0, [], target)
        return result