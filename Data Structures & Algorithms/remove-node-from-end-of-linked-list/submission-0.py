# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        reversedList = self.reverse(head)

        dummy = ListNode(0, reversedList)
        cur = dummy

        for i in range(n - 1):
            cur = cur.next

        if cur:
            cur.next = cur.next.next
        
        return self.reverse(dummy.next)

    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        return prev