# 328. Odd Even Linked List
# https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        odd = head
        even = odd.next
        evenList = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next
        
        odd.next = evenList
        return head

s = Solution()
# 10 -> 20 -> 30 -> 40 -> 50
node_10 = ListNode(10)
node_20 = ListNode(20)
node_30 = ListNode(30)
node_40 = ListNode(40)
node_50 = ListNode(50)

node_10.next = node_20
node_20.next = node_30
node_30.next = node_40
node_40.next = node_50

ans = s.oddEvenList(node_10)
while ans is not None:
    print(ans.val)
    ans = ans.next
    