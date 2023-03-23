# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        List = []
        
        while head:
            List.append(head.val)
            head = head.next

        List1 = List[:len(List)//2]
        List2 = List[len(List)//2:]
        
        if len(List) % 2 == 0:
            return True if List1 == List2[::-1] else False
        else:
            return True if List1 == List2[:0:-1] else False
        
