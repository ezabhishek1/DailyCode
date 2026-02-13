Koko can eat only 1 pile in 1 hour.
He can eat either entire pile or some Bananas from pile in 1 hour.
Suppose largest pile in whole array is of size 'hi'.
Then maximum speed of Koko can be 'hi' bananas per hour.
This will result in time equal to size of array.
Minimum speed of Koko can be 'lo' or 1 bananas per hour.
This will result in time equal to total bananas in all pile.
Aim: To find minimum speed such that time taken to finish all pile is less than or equal to k.
Approach: Binary search on all speeds from 1 to 'hi'