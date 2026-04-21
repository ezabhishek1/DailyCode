# Approach
First, check if d > max(m, n).
If yes, answer is -1.

Then check if d % gcd(m, n) != 0.
If yes, answer is -1.

Otherwise, simulate both possible directions:

Pour from m to n

Pour from n to m

In each simulation:

Fill the source jug if empty

Pour from source to target

Empty target if it becomes full

Continue until either jug contains d litres

Return the minimum operations from both simulations.