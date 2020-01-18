/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode result=new ListNode(0);
        ListNode head=result;
        int curr=0;
        while(l1.next != null || l2.next != null){
            
            int l1_val= (l1 != null) ? l1.val:0;
            int l2_val= (l2 != null) ? l2.val:0;
            
            int curr_val=l1_val+l2_val+curr;
            
            curr=curr_val/10;
            int last=curr_val%10;
            ListNode newNode=new ListNode(last);
            head.next=newNode;
            
            if(l1 != null) l1=l1.next;
            if(l2 != null) l2=l2.next;
            head=head.next;
            }
        
        if(curr > 0){
            ListNode newNode=new ListNode(curr);
            head.next=newNode;
            head=head.next;                              
        }
        
        return result.next;
    }
}