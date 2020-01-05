class Solution {
    public int numIslands(char[][] grid) {
        int count=0;
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[i].length;j++){
                if(grid[i][j]=='1'){
                    count+=1;
                    countBFS(i,j,grid);
                }
            }
            
        }
        return count;
    }
        
    public void countBFS(int i,int j, char[][] grid){
            if(i<0 || i>=grid.length || j<0 || j>=grid[i].length || grid[i][j]=='0')
                return;
            
            grid[i][j]='0';
        
            countBFS(i+1,j,grid);
            countBFS(i-1,j,grid);
            countBFS(i,j+1,grid);
            countBFS(i,j-1,grid);
           
        }
}