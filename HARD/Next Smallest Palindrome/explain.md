simple Intuition 

- A palindrome is determined by its left half, so first mirror the left side to the right to get the closest palindrome.
- If this mirrored number is already greater than the original, it is the answer.
-- Otherwise, increase the middle digit(s) and propagate any carry toward the left, mirroring changes to maintain the palindrome.
