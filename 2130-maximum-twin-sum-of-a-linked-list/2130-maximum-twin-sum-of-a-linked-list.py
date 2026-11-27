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
        
        if slow.next == None:
            return head.val + head.next.val

        temp = slow

        while temp != None:
            stack.append(temp.val)
            temp = temp.next

        ptr = head
        while ptr != slow:
            max_len = max(max_len, ptr.val + stack.pop())
            ptr = ptr.next
        
        return max_len