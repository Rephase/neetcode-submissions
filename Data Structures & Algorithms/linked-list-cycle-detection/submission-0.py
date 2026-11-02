# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = [] # keep track of visted nodes
        temp = head # make copy

        # while temp isn't null
        while temp: 
            if temp in visited:
                # found the cycle
                return True 
            else:
                visited.append(temp)
                temp = temp.next
        
        return False
        