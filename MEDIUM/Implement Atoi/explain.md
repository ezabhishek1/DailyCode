# i) Intuition:
The goal is to convert a string into an integer, just like the atoi function in C. The function should skip leading whitespaces, handle optional '+' or '-' signs, read in the numeric characters, and stop at the first non-digit. If the number goes beyond the 32-bit signed integer range, it should be clamped accordingly.

ii) Approach:

Start by skipping all the leading whitespaces using a simple for loop.

Then, check if the current character is '+' or '-' and update the sign.

Iterate over the remaining characters:

If the character is a digit, convert it to an integer using ch - '0'.

Before adding it to the number, check if it will cause overflow using the condition:
num > (Integer.MAX_VALUE - digit) / 10

If overflow is possible, return Integer.MAX_VALUE or Integer.MIN_VALUE depending on the sign.

Otherwise, update num = num * 10 + digit.

Stop parsing when a non-digit character is found.

