Easy to understand code in Java. I am using the formula of grey code = i^(i/2).
I am using the toBinaryString() method to convert decimal numbers to binary numbers in a formatted way. 

star the repo ⭐ if you understand and find it easy.


Approach
I loop from 0 to (1 << n) - 1.

For every number i, I calculate its Gray Code value using:

gray = i ^ (i >> 1)

I convert that Gray Code value into a binary string.

If the binary string length is smaller than n, I add leading zeroes.

I store every binary string in the answer list.

Finally, I return the list.

----------------------------------