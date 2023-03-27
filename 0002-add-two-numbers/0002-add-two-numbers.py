# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        pointer = ans
        
        num1 = 0
        num2 = 0
        i = 1
        
        while l1:
            num1 += l1.val * i
            i *= 10
            l1 = l1.next
        i = 1
        while l2:
            num2 += l2.val * i
            i *= 10
            l2 = l2.next
            
        num = num1 + num2
        if num == 0:
            ans.val = 0
            return ans
        
        while num > 0:
            node = ListNode()
            node.val = num % 10
            num //= 10
            
            ans.next = node
            ans = ans.next
            
        return pointer.next