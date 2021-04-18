# 206. Reverse Singly Linked List
# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node = None
        while head is not None:
            next = head.next
            head.next = node
            node = head
            head = next
        return node

s = Solution()
node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(3)
node_4 = ListNode(4)
node_5 = ListNode(5)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5

answer = s.reverseList(node_1)
while answer != None:
    print(answer.val)
    answer = answer.next
    


