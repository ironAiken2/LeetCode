# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        p = head
        
        p2 = p.next
        p.next = p2.next
        p2.next = p
        
        save = p
        p = p.next
        
        head = p2
        
        while p:
            if not p or not p2 or not p.next or not p2.next:
                break
            
            p2 = p.next
            p.next = p2.next
            p2.next = p
            save.next = p2
            save = p
            
            p = p.next
            
        return head
            