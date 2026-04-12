# Intuition:-

 Comparing current element with its respective diagonal element if it is not equal with the previous diagonal element then matrix is not Toeplitz ,otherwise it is Toeplitz matrix
 
 
 ## Given Test Case :
 
 ![alt text](93ceca32-c80e-4dac-ad96-1ed562e5aee6_1719430600.png)

 ## Implementation :

 ![alt text](684068dd-0bf5-41b6-b48c-d8fa961a730c_1719430976.jpg)


 ## Algorithm:

-- 1)Declare n and m which is the total number of rows present in the matrix and total number of columns present in the matrix.

-- 2)Outer loop runs for (i<n) 

Inner  loop runs for (j<m)  and inside this  loop checking the invalid condition (i!=0  && j!=0) because we have to check with mat[i-1][j-1] so i-1>=0 and j-1>=0.
 if diagional element is not equal with current element return false.
3) At the end it must be a Toeplitz matrix so return true.