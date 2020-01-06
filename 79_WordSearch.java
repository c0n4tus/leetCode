class Solution {
    public boolean visited[][];
    public boolean exist(char[][] board, String word) {
        visited=new boolean[board.length][board[0].length];
        for(int i=0;i<board.length;i++){
            for(int j=0;j<board[i].length;j++){
                if(board[i][j] == word.charAt(0) && searchWord(i,j,board,word,0)){
                    return true;
                }
            }
        }
        
        return false;
    }
    
    public boolean searchWord(int i,int j, char[][] board, String word, int index){
        if(index == word.length()){
            return true;
        }
        
        
if(i<0 || i>= board.length || j<0 || j>= board[i].length || word.charAt(index) != board[i][j] || visited[i][j]){
            return false;
        }
       
        
        visited[i][j]=true;
        if(
        searchWord(i+1,j,board,word,index+1) ||
        searchWord(i-1,j,board,word,index+1) ||
        searchWord(i,j+1,board,word,index+1) ||
        searchWord(i,j-1,board,word,index+1) ){
            return true;
        }
        visited[i][j]=false;
        return false;
        
    }
}