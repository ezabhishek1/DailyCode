# Approach

I used a hash map to store every string and its index.

Then for every word:

- I tried every possible split position.

- From that split, I got:

    - left substring

    - right substring

- I checked two cases.

## Case 1:

- If the left part is palindrome,

- then I searched for reverse of the right part in the map.

- If it exists and belongs to another index, then a valid pair exists.

## Case 2:

- If the right part is palindrome,

- then I searched for reverse of the left part.

- If it exists and belongs to another index, then a valid pair exists.

If any valid pair is found, I return true.

If all checks finish and nothing works, I return false.