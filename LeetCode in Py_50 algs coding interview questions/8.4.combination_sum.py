# https://leetcode.com/problems/combination-sum/
# 39. Combination Sum

class Solution:
    def solution(candidates, ans, curr, target, index, sum):
      if sum == target:
        ans.append(curr[:])
      elif sum < target:
        n = len(condidates)
        for i in range(index, n):
          curr.append(candidates[i]):
          self.solution(candidates, ans, curr, target, i, sum + candidates[i])
          curr.pop()
      return
                               
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        curr = []
        self.solution(candidates, ans, curr, target, 0, 0)
        return ans
