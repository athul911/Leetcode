import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        heap = []

        current_node_1 = list1
        current_node_2 = list2
        while current_node_1 or current_node_2:
            if current_node_1:
                heapq.heappush(heap,current_node_1.val)
                current_node_1 = current_node_1.next
            if current_node_2:
                heapq.heappush(heap,current_node_2.val)
                current_node_2 = current_node_2.next
        
        dummyhead = ListNode(0)
        current = dummyhead
        while heap:
            value =  heapq.heappop(heap)
            current.next = ListNode(value)
            current = current.next
        
        return dummyhead.next