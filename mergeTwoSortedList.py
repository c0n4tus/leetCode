# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        dum=ListNode
        dum.next=None
        dum.val=None
        head1=l1
        head2=l2
        headN=dum
        if head1 != None:
            while head1 != None:
                if head2 != None:
                    if head1.val < head2.val:
                        n1=head1
                        head1=head1.next
                        n1.next=None
                        dum.next=n1
                        dum=dum.next
                        if head1 == None and head2 != None:
                            dum.next=head2
                            break
                    elif head2.val < head1.val:
                        n1=head2
                        head2=head2.next
                        n1.next=None
                        dum.next=n1
                        dum=dum.next
                        if head2 == None and head1 != None:
                            dum.next=head1
                            break
                    else:
                        n1=head1
                        n2=head2
                        head2=head2.next
                        head1=head1.next
                        n1.next=n2
                        n2.next=None
                        dum.next=n1
                        dum=dum.next.next
                        if head1 == None and head2 != None:
                            dum.next=head2
                            break
                        if head2 == None and head1 != None:
                            dum.next=head1
                            break
                elif head2 == None:
                    dum.next=head1
                    break
        else:
            dum.next=head2 
                
        return headN.next