# 881. Boats to Save People
# https://leetcode.com/problems/boats-to-save-people/

# Initialize 2 pointers, left at the beginning of the array
# and right at the end of the array
# loop as long as the right pointer is bigger than or equal to the left pointer
from typing import List

# Time complexity: O(Nlog(N))
# Space complexity: O(N)
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        numBoats = 0
        left, right = 0, len(people) - 1

        while left <= right:
            if left == right:
                numBoats += 1
                break
            
            if people[left] + people[right] <= limit:
                left += 1
                
            right -= 1
            numBoats += 1

    # same 
    def numRescueBoats_(self, people: List[int], limit: int) -> int:
        people.sort()
        numBoats = 0
        left, right = 0, len(people) - 1

        while left < right:
            if people[left] + people[right] <= limit:
                left += 1
            numBoats += 1
            right -= 1
        
        if left == right:
            numBoats += 1
        
        return numBoats

s = Solution()
print(s.numRescueBoats([3,5,3,4], 5))