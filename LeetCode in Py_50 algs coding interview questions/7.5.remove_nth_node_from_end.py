# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ans = ListNode(0)
        ans.next = head
        
        first = ans 
        second = ans
        for i in range(1, n + 2):
            first = first.next
        
        while first is not None:
            first = first.next
            second = second.next
        
        second.next = second.next.next

        return ans.next
    
    def removeNthFromEnd_(self, head: ListNode, n: int) -> ListNode:
        first = second = head
        for _ in range(n):
            first = first.next
        
        if not first:
            return head.next
        
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return head
    
s = Solution()
# 1 -> 3 -> 5 -> 7, n = 2
node_1 = ListNode(1)
node_3 = ListNode(3)
node_5 = ListNode(5)
node_7 = ListNode(7)

node_1.next = node_3
node_3.next = node_5
node_5.next = node_7

ans = s.removeNthFromEnd(node_1, 2)
while ans != None:
    print(ans.val)
    ans = ans.next