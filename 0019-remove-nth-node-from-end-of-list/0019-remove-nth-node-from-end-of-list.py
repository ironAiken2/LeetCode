# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p = head
        length = 0
        
        while p:
            length += 1
            p = p.next
        
        if length == n:
            return head.next
        
        p = head
        
        while length != n+1 and p:
            p = p.next
            length -= 1
            
        p.next = p.next.next
        
        return head