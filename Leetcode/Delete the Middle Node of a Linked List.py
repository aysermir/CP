# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        le = 0
        if head == None or head.next == None:
            return None
        pointer = head
        while pointer:
            le+=1
            pointer = pointer.next
        mid =int(le/2)
        p = head
        for i in range(0, mid-1):
            p=p.next
        x = p.next
        if x!=None:
            p.next = x.next
        return head

        
