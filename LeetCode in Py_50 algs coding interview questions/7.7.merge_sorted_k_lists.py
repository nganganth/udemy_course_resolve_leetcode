# https://leetcode.com/problems/merge-k-sorted-lists/
# 23. Merge k Sorted Lists

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        curr = ListNode(0)
        ans = curr

        while l1 and l2:
            if l1.val > l2.val:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next
            curr = curr.next
        
        while (l1):
            curr.next = l1
            l1 = l1.next
            curr = curr.next
        
        while (l2):
            curr.next = l2
            l2 = l2.next
            curr = curr.next

        return ans.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        
        i = 0
        last = len(lists) - 1
        j = last

        while last != 0:
            i = 0
            j = last
            while j > i:
                lists[i] = self.mergeTwoLists(lists[i], lists[j])
                i += 1
                j -= 1
                last = j
        return lists[0]
    
    
