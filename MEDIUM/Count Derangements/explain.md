# Understanding Derangements (Subfactorial)

- A Derangement is a permutation of $n$ elements such that no element appears in its original position. Let $D(n)$ be the number of derangements for $n$ elements.

# The Recursive Intuition
- Suppose we have $n$ elements, and we want to place the first element (let's call it Ball 1) into a wrong position. There are $(n - 1)$ possible positions for Ball 1 (any position except index 1).

Let’s say we place Ball 1 into Position $i$ (where $i \neq 1$). Now, we look at what happens to Ball $i$:

## Case 1: Ball $i$ moves to Position 1
The Swap: Ball 1 is in Position $i$, and Ball $i$ is in Position 1.

They have "swapped" spots, effectively neutralizing each other.

Remaining Task: we now need to derange the remaining $(n - 2)$ elements.

Ways: $D(n - 2)$.

