# Approach
If x == 1, return whether y == 1

Keep dividing y by x while y % x == 0

After all divisions:

If y == 1, return true

Otherwise, return false

This works because a valid power of x can always be reduced to 1 after repeated division.