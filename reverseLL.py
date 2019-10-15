# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr=head
        if curr is None:
            return None
        next1=head.next
        prev=None
        while curr is not None:
            curr.next=prev
            prev=curr
            curr=next1
            if curr is not None:
                next1=curr.next
            else:
                next1=None
            
        
        head=prev
        return head