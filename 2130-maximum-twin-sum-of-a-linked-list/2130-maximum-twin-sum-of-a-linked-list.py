# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        slow, fast = head, head

        stack = []
        max_len = float('-inf')

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        # If slow is at end, meaning only 2 items, return just the sum.
        if slow.next == None:
            return head.val + head.next.val

        # Reversing
        ptr = slow
        while ptr != None:
            stack.append(ptr.val)
            ptr = ptr.next

        # Calculating max twin
        ptr = head
        while ptr != slow:
            max_len = max(max_len, ptr.val + stack.pop())
            ptr = ptr.next
        
        return max_len