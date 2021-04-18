# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(None)
        pointer:ListNode = ans
        carry = 0
        _sum = 0

        while l1 != None or l2 != None:
            _sum = carry
            if l1 != None:
                _sum += l1.val
                l1 = l1.next
            
            if l2 != None:
                _sum += l2.val
                l2 = l2.next
            
            carry = int(_sum/10)
            pointer.next = ListNode(_sum%10)
            pointer = pointer.next
        
        if carry > 0:
            pointer.next = ListNode(carry)
        
        return ans.next
    
    def addTwoNumbers_(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = n = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            val1 = val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            sumVal = val1 + val2 + carry
            carry, val = sumVal//10, sumVal%10
            n.next = ListNode(val)
            n = n.next
        return res.next


s = Solution()
# 2 -> 4 -> 3
l1_node_2 = ListNode(2)
l1_node_4 = ListNode(4)
l1_node_3 = ListNode(3)
l1_node_2.next = l1_node_4
l1_node_4.next = l1_node_3

# 5 -> 6 -> 4
l2_node_5 = ListNode(5)
l2_node_6 = ListNode(6)
l2_node_4 = ListNode(4)
l2_node_5.next = l2_node_6
l2_node_6.next = l2_node_4

ans = s.addTwoNumbers(l1_node_2, l2_node_5)
while ans != None:
    print(ans.val)
    ans = ans.next
