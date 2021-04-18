# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        hare = head
        turtle = head

        while turtle and hare and hare.next:
            hare = hare.next.next
            turtle = turtle.next
            if turtle == hare:
                return True
        return False

s = Solution()
# 1 -> 5 -> 11 -> 8 -> 9 -> 5 -> 11 ....
node_1 = ListNode(1)
node_5 = ListNode(5)
node_11 = ListNode(11)
node_8 = ListNode(8)
node_9 = ListNode(9)

node_1.next = node_5
node_5.next = node_11
node_11.next = node_8
node_8.next = node_9
node_9.next = node_5

print(s.hasCycle(node_1))
