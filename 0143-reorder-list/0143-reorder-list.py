class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        
        # Step 1: Split the list into two halves
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half of the list
        prev = None
        current = slow
        
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        # Merge the two halves in-place
        first_half = head
        second_half = prev
        
        while second_half.next:
            temp = first_half.next
            first_half.next = second_half
            first_half = temp
            
            temp = second_half.next
            second_half.next = first_half
            second_half = temp
