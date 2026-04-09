class Solution {
    ArrayList<Integer> intersection(int[] a, int[] b) {
        // code here
        HashSet<Integer> set = new HashSet<>();
        
        for(int n2 : b){
            set.add(n2);
        }
        ArrayList<Integer> res = new ArrayList<>();
        
        for(int n1 : a){
            if(set.contains(n1)){
                res.add(n1);
                set.remove(n1);
            }
        }
        return res;
    }
}