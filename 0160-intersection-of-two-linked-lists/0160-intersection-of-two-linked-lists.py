# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        list1 = []
        list2 = []
        
        while headA and headB:
            list1.append(headA)
            list2.append(headB)
            
            headA = headA.next
            headB = headB.next
            
        while headA:
            list1.append(headA)
            headA = headA.next
        while headB:
            list2.append(headB)
            headB = headB.next
    
        cur = None
        
        for data in zip(reversed(list1), reversed(list2)):
            if data[0] == data[1]:
                cur = data[0]
            else:
                break
                
        return cur
                
            
        