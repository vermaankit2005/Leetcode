# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:

        temp_node = ListNode(-1, None)
        head = temp_node
        ptr = temp_node
        while list1 != None and list2 != None:
            
            if list1.val <= list2.val:
                ptr.next = list1
                list1 = list1.next
                ptr = ptr.next
                ptr.next = None
            else:
                ptr.next = list2
                list2 = list2.next
                ptr = ptr.next
                ptr.next = None
          

        if list1 != None:
            ptr.next = list1
        if list2 != None:
            ptr.next = list2 
        
        return head.next