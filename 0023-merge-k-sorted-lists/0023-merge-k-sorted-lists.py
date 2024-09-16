# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap,(lists[i].val,i,lists[i]))
        

        head = ListNode(0)
        current = head

        while heap:
            value,i,node = heapq.heappop(heap)
            current.next = ListNode(value)
            current = current.next
            if node.next:
                heapq.heappush(heap,(node.next.val,i,node.next))
        
        return head.next
