# https://leetcode.com/problems/missing-number/
# 268. Missing Number

# Mathematical approach: gauss formula
# s = 1 + 2 + ... + (n-1) + n
# s = n + (n-1) + ... + 2 + 1
# s = n*(n+1)/2
class Solution:
    # normal way 
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i range(0, n):
            if i not in nums:
                return i
    
    # using gauss formula
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        intendedSum = n*(n+1)//2
        return intendedSum - sum(nums) 
            