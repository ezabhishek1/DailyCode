class Solution {
    public boolean isWordExist(char[][] mat, String word) {
        // Code here
        int m = mat.length, n=mat[0].length;
        
        for(int i=0; i<m; i++)
        {
            for(int j=0; j<n; j++)
            {
                if(word.charAt(0)==mat[i][j] && foundWord(0,i,j,word,mat))
                return true;
            }
        }
        return false;
    }
    
    boolean foundWord(int index, int i, int j, String word, char[][] mat)
    {
        if(index==word.length()) return true;
        if(i<0 || j<0 || i>=mat.length || j>=mat[0].length) return false;
        
        boolean f = false;
        if(mat[i][j]!='#' && mat[i][j]==word.charAt(index)) {
            char temp = mat[i][j];
            mat[i][j] = '#';
            
            f = foundWord(index+1,i+1,j,word,mat) ||
                foundWord(index+1,i-1,j,word,mat) || 
                foundWord(index+1,i,j+1,word,mat) || 
                foundWord(index+1,i,j-1,word,mat);
                        
            mat[i][j] = temp;
        }
        return f;
    }
}
