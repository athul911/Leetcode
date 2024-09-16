# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        list2 = []
        while True:
            if not l1 and not l2:
                break
            if l1 is not None:
                list1.append(l1.val)
                l1 = l1.next
            if l2 is not None:
                list2.append(l2.val)
                l2 = l2.next

        number1 = "".join(str(item) for item in list1[::-1])
        number2 = "".join(str(item) for item in list2[::-1])
        newsum = str(int(number1)+int(number2))
        llist = ListNode(0)
        curr_node = llist
        for num in newsum[::-1]:
            curr_node.next = ListNode(num)
            curr_node = curr_node.next
        llist = llist.next
        return llist
