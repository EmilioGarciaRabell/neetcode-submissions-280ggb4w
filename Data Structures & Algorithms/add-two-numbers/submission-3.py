# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1str = ""
        l2str = ""

        curr = l1
        while curr:
            l1str += str(curr.val)
            curr = curr.next
        curr = l2
        while curr:
            l2str += str(curr.val)
            curr = curr.next
        
        l1str = l1str[::-1]
        l2str = l2str[::-1]

        l1PlusL2 = int(l1str) + int(l2str)
        l1PlusL2 = str(l1PlusL2)[::-1]

        headRes = ListNode(l1PlusL2[0])

        curr = headRes
        for i in range(1,len(l1PlusL2)):
            curr.next = ListNode(l1PlusL2[i])
            curr = curr.next
        
        return headRes