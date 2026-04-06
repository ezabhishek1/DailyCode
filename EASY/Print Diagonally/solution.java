class Solution{
    public static ArrayList<Integer> diagView(int mat[][]){
        ArrayList<Integer> al=new ArrayList<>();
        for(int i=0;i<mat.length;i++){
            int idx1=0,idx2=i;
            while(idx1<mat.length && idx2>=0){
                al.add(mat[idx1++][idx2--]);
            }
        }
        for(int i=1;i<mat.length;i++){
            int idx1=i,idx2=mat.length-1;
            while(idx1<mat.length && idx2>=0){
                al.add(mat[idx1++][idx2--]);
            }
        }
        return al;
    }
}