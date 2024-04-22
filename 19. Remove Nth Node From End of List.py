# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        if n == 0:
            return head
        curr = head
        while(curr!=None):
            length+=1
            curr = curr.next
        rem_node_index = length - n
        if rem_node_index == 0:
            return head.next
        res = head
        i = 1
        while(i < rem_node_index):
            res = res.next
            i+=1
        res.next = res.next.next

        return head
        