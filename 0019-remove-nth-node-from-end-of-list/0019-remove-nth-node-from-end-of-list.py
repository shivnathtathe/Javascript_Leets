# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
      
        if not head:
            return None

        a = ListNode(0)
        a.next = head
        first = a
        second = a

    
        for i in range(n + 1):
            first = first.next

      
        while first is not None:
            first = first.next
            second = second.next

        
        second.next = second.next.next

        return a.next
