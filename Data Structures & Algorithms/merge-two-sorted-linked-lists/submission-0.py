# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if (not list1):
            # if first list empty, just return second list
            return list2
        elif (not list2):
            # and vice versa
            return list1
        
        if list1.val <= list2.val:
            # if heads are equal, just place either one into merged
            # if head of list1 is less than list2, place list1 head at head of merged
            return ListNode(list1.val,
            self.mergeTwoLists(list1.next, list2)) # recursive call for next node of merged
        elif list2.val < list1.val:
            return ListNode(list2.val,
            self.mergeTwoLists(list1, list2.next))
