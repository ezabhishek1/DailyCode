class Solution {
    public boolean isPower(int x, int y) {
        if(x == 1 && y > x)
        {
            return false;
        }
        boolean flag = false;
        for(int i = 0; i < y; i++)
        {
            int pow = (int)Math.pow(x, i);
            if(pow == y)
            {
                flag = true;
                break;
            }
            if(pow > y)
            {
                break;
            }
        }
        return flag;
    }
}
