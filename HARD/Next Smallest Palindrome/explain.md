# simple Intuition 

- A palindrome is determined by its left half, so first mirror the left side to the right to get the closest palindrome.
- If this mirrored number is already greater than the original, it is the answer.
-- Otherwise, increase the middle digit(s) and propagate any carry toward the left, mirroring changes to maintain the palindrome.



# Approach
## I first check whether every digit is 9.

If yes, I return 1 followed by all 0s and then 1.

## I compare the left half and the right half from the center outward.

This helps me know whether the mirrored palindrome will already be bigger or not.

## I mirror the left side to the right side.

This gives me the nearest palindrome based on the left half.

## If the original number was already bigger on the left side, that mirrored result is the answer.

Otherwise, I increase the middle digit(s) by 1.

If there is a carry, I keep moving left and updating digits.

After every change on the left side, I copy that digit to the right side.

## Finally, I return the updated array.

