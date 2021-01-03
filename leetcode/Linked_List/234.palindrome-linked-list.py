# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q: Deque = collections.deque()
            
        if not head:
            return True
        
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next
            
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
            
        return True

''' 
slow, fast 런너를 이용한 풀이법

def isPalindrome(self, head: ListNode) -> bool:
    rev = None
    slow = fast = head
    # 런너를 이용해 역순 연결 리스트 구성
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    # 입력값이 홀수일 경우 중앙값을 제외 처리 
    if fast:
        slow = slow.next
    
    # 팰린드롬 여부 확인
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev