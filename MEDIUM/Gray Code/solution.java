class Solution
{
    public ArrayList<String> graycode(int n)
    {
        ArrayList<String> al = new ArrayList<>();
        if(n==1){
            al.add("0");
            al.add("1");
            return al;
        }
        int limit = (int)Math.pow(2,n)-1;
        al.add(parse(0,n));
        for(int i=1;;i++){
            int grey = i^(i/2);
            if(grey>limit){
                break;
            }
            al.add(parse(grey,n));
        }
        return al;
    }
    
    public static String parse(int decimal,int n){
        String binary = Integer.toBinaryString(decimal);
        if (binary.length() < n) {
            binary = "0".repeat(n - binary.length()) + binary;
        }
        return binary;
    }
}