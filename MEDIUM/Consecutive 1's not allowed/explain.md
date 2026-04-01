Simple recursion and dp.
We do not have to store the string , we jsut have to store the string size (here "strSize") and last element (prev) of the string.
If prev==1, we have to add "0" as next element in the string, so there is only one case.
If prev==0, we can add "0" or "1" as next element of the string, so there will be two cases.
Add all the cases to get answer.
Recursion ends when strSize==n.