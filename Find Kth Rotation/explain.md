💡 Approach (Simple Linear Scan)
The array given is a sorted array that has been rotated.
In such an array, the number of rotations is equal to the index of the minimum element.

🔍 Key Observation
In a sorted array, elements increase continuously.

After rotation, there will be exactly one point where the order breaks:

 
arr[i] > arr[i+1]
The element at i+1 is the smallest element, and i+1 gives the number of rotations.

🛠️ Algorithm
Traverse the array from index 0 to n-2.

Check if arr[i] > arr[i+1].

If found, return i + 1 as the rotation count.

If no such point exists, the array is not rotated → return 0.

⏱️ Time & Space Complexity
Time Complexity: O(n)

Space Complexity: O(1)