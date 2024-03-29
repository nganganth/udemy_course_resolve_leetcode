# https://leetcode.com/problems/subsets/
# 78. Subsets

class Solution:
    def solution(self, nums, ans, cur, index):
            if index > len(nums):
                return
            ans.append(cur[:])
            for i in range(index, len(nums)):
                if nums[i] not in cur:
                    cur.append(nums[i])
                    self.solution(nums, ans, cur, i)
                    cur.pop()
    def subsets(self, nums: List[int]) -> List[List[int]]:
        cur = []
        ans = []
        self.solution(nums, ans, cur, 0)
        return ans

        
