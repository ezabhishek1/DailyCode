# Mathematical Intuition

Let the sum of all elements assigned a + sign be $S_1$ and the sum of all elements assigned a - sign be $S_2$. We are looking for:

$S_1 - S_2 = \text{target}$

$S_1 + S_2 = \text{totalSum}$

Adding these two equations gives:

$2S_1 = \text{target} + \text{totalSum}$

$S_1 = \frac{\text{target} + \text{totalSum}}{2}$

Therefore, the problem reduces to finding the number of subsets that sum up to $S_1$.

# Key Constraints & Edge Cases

Validity: If $(\text{target} + \text{totalSum})$ is odd or if $\text{abs(target)} > \text{totalSum}$, it is impossible to form the target sum. Return 0.

Zeros: If the array contains zeros, they double the number of ways for each subset (as $+0$ and $-0$ are distinct expressions).