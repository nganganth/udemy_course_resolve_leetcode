# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# using sliding window technique
# if ele exits in the map, set the left pointer to the position of the next possible start    
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        left, right = 0, 0
        ans = 0
        n = len(s)
        while(left < n and right < n):
            el = s[right]
            if el in m:
                left = max(left, m[el] + 1)
            m[el] = right
            ans = max(ans, right - left + 1)
            right += 1
        return ans
