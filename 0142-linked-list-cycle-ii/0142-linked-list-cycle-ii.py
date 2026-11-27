# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None:
            return head

        slow, fast = head, head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: 
                # meaning a cycle exist
                break
        
        # Check if loop break because the fast reached to the end
        if fast == None or fast.next == None:
            return None
        
        slow_ptr = head

        while slow != slow_ptr:
            slow = slow.next
            slow_ptr = slow_ptr.next

        return slow
        