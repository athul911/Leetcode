# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        vals = []
        current_node = head
        while current_node:
            vals.insert(0,current_node.val)
            current_node = current_node.next
        
        vals.pop(n-1)
        print(vals)
        new_ll = ListNode(0)
        new_node = new_ll
        for val in vals[::-1]:
            new_node.next = ListNode(val)
            new_node = new_node.next
        
        return new_ll.next