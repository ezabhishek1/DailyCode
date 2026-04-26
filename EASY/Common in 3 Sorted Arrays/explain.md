## Approach
- I keep one pointer for each array: i, j, and k.

- I compare a[i], b[j], and c[k].

- If all three are equal:

-- I add that value to the answer only if it is not already the last inserted value.

-- Then I move all three pointers forward.

- If they are not equal:

-- I find the smallest of the three values.

-- I move forward every pointer that has that smallest value.

- I repeat this until one array ends.

- The final list contains all common elements in sorted order.