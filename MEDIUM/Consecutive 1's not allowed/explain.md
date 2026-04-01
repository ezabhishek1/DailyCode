Simple recursion and dp.
We do not have to store the string , we jsut have to store the string size (here "strSize") and last element (prev) of the string.
If prev==1, we have to add "0" as next element in the string, so there is only one case.
If prev==0, we can add "0" or "1" as next element of the string, so there will be two cases.
Add all the cases to get answer.
Recursion ends when strSize==n.



# Approach
---   Let:

endWith0 = number of valid strings ending with 0

endWith1 = number of valid strings ending with 1

For length 1:

"0" → ends with 0

"1" → ends with 1

So:

endWith0 = 1

endWith1 = 1

For every next position:

New strings ending with 0 can come from both previous 0 and 1

New strings ending with 1 can only come from previous 0

So:

newEndWith0 = endWith0 + endWith1

newEndWith1 = endWith0

Update the values for every length from 2 to n.

Final answer is:

endWith0 + endWith1