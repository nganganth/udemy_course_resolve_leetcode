# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = ListNode(0)
        ans = cur

        while l1 and l2:
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next

            cur = cur.next

        while l1:
            cur.next = l1
            l1 = l1.next
            cur = cur.next
        
        while l2:
            cur.next = l2
            l2 = l2.next
            cur = cur.next
        
        return ans.next
    
s = Solution()
l1_1 = ListNode(1)
l1_2 = ListNode(2)
l1_3 = ListNode(3)
l1_1.next = l1_2
l1_2.next = l1_3

l2_1 = ListNode(1)
l2_2 = ListNode(3)
l2_3 = ListNode(4)
l2_1.next = l2_2
l2_2.next = l2_3

answer = s.mergeTwoLists(l1_1, l2_1)
print(answer)

while answer != None:
    print(answer.val)
    answer = answer.next


        