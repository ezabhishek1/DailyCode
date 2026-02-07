Algorithm:
Initialize Variables

Set max = arr[0] (stores max product ending at current index).
Set min = arr[0] (stores min product ending at current index, needed for negative values).
Set bossMax = arr[0] (stores the overall maximum product found so far).
Iterate Through the Array (from index 1 to n-1):

Compute potential max and min products at the current index:
a = arr[i] * max
b = arr[i] * min
Update max as the maximum of (a, b, arr[i]).
Update min as the minimum of (a, b, arr[i]).
Update bossMax as the maximum of bossMax and max.
Return bossMax as the result.