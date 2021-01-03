# https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        l1 = odd = ListNode(0)
        l2 = even = ListNode(0)
        
        i=1
        while head:
            if i%2:
                odd.next, odd = head, head
            else:
                even.next, even = head, head
            head = head.next
            i += 1
        odd.next, even.next = l2.next, None
        return l1.next
