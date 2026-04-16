# i) Intuition:
The goal is to convert a string into an integer, just like the atoi function in C. The function should skip leading whitespaces, handle optional '+' or '-' signs, read in the numeric characters, and stop at the first non-digit. If the number goes beyond the 32-bit signed integer range, it should be clamped accordingly.

ii) Approach:

Start by skipping all the leading whitespaces using a simple for loop.



