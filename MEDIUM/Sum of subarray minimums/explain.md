##Hint 1: Think in terms of contribution

Instead of enumerating all subarrays, ask:
For each element arr[i], in how many subarrays is it the minimum?
If you can count that, then its contribution to the total sum is simply:
arr[i] * (number of subarrays where arr[i] is minimum)


Hint 2: Boundaries of influence
For each element, you need to know:
- How far left you can extend before hitting a smaller element.
- How far right you can extend before hitting a smaller element.
That defines the range of subarrays where arr[i] is the minimum.


Hint 3: Use monotonic stacks
To find those boundaries efficiently:
- Use a monotonic stack to compute the previous smaller element for each index.
- Use another monotonic stack to compute the next smaller element for each index.