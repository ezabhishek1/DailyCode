# Approach

- I started with the idea that all tasks go to machine B first. That gives me a base profit of sum(b).

## Then I computed a difference for every task:

- - diff[i] = a[i] - b[i]

- This tells me how much extra profit I get if I move task i from B to A.

- After that, I sorted all differences in descending order. That way, the best tasks to move to A come first.

- If I choose k tasks for A, then the best gain for that k is the sum of the first k differences in sorted order. I only need to check values of k that are allowed.

## The allowed range is simple:

- At least n - y tasks must go to A, because B can handle at most y tasks.

- At most x tasks can go to A, because A has capacity x.

- So I scanned the sorted differences once, kept a running sum, and checked every valid task count. The best running sum in that range was the extra profit I needed. I then added that to the base profit.