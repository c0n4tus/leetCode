# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        count=0
        node=head
        newHead=head
        nodeToMaintain=head
        while node.next != None:
            node=node.next
            count+=1
        
        if count == 0 and n == 1:
            head=None
            return head
        elif (count-n+1) == 0:
            nodeToMaintain=newHead.next
            newHead=None
            return nodeToMaintain
            
        for i in range(0,(count-n+1)):
            nodeToMaintain=newHead
            newHead=newHead.next
        if newHead.next == None:
            nodeToMaintain.next=None
            newHead=None
        else:
            nodeToMaintain.next=newHead.next
            newHead=None
            
        
        return head
            