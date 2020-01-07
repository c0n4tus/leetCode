/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        
        List<Integer> values=new ArrayList<Integer>();
        Stack<TreeNode> st=new Stack<>();
        
        if(root == null){
            return values;
        }
        
        TreeNode curr=root;
        //st.add(curr);
        while(curr != null || !st.isEmpty()){
            while(curr != null){
                st.push(curr);
                curr=curr.left;
            }
            curr=st.pop();
            values.add(curr.val);
            curr=curr.right;
        }
        return values;
    }
}