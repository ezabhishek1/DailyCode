# Sort by Set Bit Count - Beginner Explanation

## Problem overview

The goal is to sort a list or array of integers so that numbers with more set bits (1s in their binary representation) come before numbers with fewer set bits.

Example:
- `5` in binary is `101` → 2 set bits
- `3` in binary is `11` → 2 set bits
- `2` in binary is `10` → 1 set bit
- `7` in binary is `111` → 3 set bits

After sorting by set bit count descending, `7` should come before `5` and `3`, and `2` should come last.

## Common idea in all solutions

All three implementations do the same basic thing:

1. Count how many `1` bits each number has.
2. Use that count as the sorting key.
3. Sort the numbers so the highest counts come first.

The main difference is the language-specific way of counting bits and sorting.

## Python solution explanation

```python
class Solution:
    def sortBySetBitCount(self, arr):
        # bin(x).count('1') returns the number of set bits
        # reverse=True ensures descending order
        arr.sort(key=lambda x: bin(x).count('1'), reverse=True)
        return arr
```

Step by step:
- `bin(x)` converts an integer `x` into a binary string like `'0b101'`.
- `.count('1')` counts the number of `'1'` characters in that string.
- `arr.sort(...)` sorts the list in place.
- `key=lambda x: bin(x).count('1')` tells Python to compare numbers by their bit count instead of by the number itself.
- `reverse=True` means the sort order is descending, so bigger counts come first.

Why this is good for beginners:
- Python's `sort` with `key` is easy to read.
- The bit count is computed directly using built-in tools.
- The code is short and clear.

## C++ solution explanation

```cpp
class Solution {
  public:
    vector<int> sortBySetBitCount(vector<int>& arr) {
        vector<vector<int>> bits(33);
        for(int i : arr) bits[__builtin_popcount(i)].push_back(i);

        vector<int> ans;
        for(int b = 32; b >= 0; b--) for(int i : bits[b]) ans.push_back(i);

        return ans;
    }
};
```

Step by step:
- `vector<vector<int>> bits(33);` creates 33 buckets, one for each possible number of set bits from `0` to `32`.
- `__builtin_popcount(i)` returns the number of 1 bits in the integer `i`.
- `bits[count].push_back(i);` stores each number in the bucket for its bit count.
- After grouping, the code builds the result by iterating from `b = 32` down to `0`.
- Numbers in the same bucket are kept in the same order they appeared in the input, which preserves stability.

Why this is good for beginners:
- It avoids a custom sort comparator and uses a simple bucket approach.
- It makes the concept of grouping by bit count easy to follow.
- `__builtin_popcount` is a direct way to count bits in C++.

## Java solution explanation

```java
class Solution {
     public ArrayList<Integer> sortBySetBitCount(int[] arr) {
        int n = arr.length;

        // Convert to Integer[]
        Integer[] temp = new Integer[n];
        for (int i = 0; i < n; i++) {
            temp[i] = arr[i];
        }

        // Stable sort
        Arrays.sort(temp, (a, b) -> {
            return Integer.bitCount(b) - Integer.bitCount(a);
        });

        // Convert to ArrayList
        ArrayList<Integer> result = new ArrayList<>();
        for (int num : temp) {
            result.add(num);
        }

        return result;
    }
}
```

Step by step:
- `int[] arr` is the input array of primitive integers.
- Java's `Arrays.sort` with a comparator only works on object arrays, so first the code converts `int[]` to `Integer[]`.
- `Integer.bitCount(x)` returns the number of 1 bits in `x`.
- The comparator `(a, b) -> Integer.bitCount(b) - Integer.bitCount(a)` sorts in descending order by bit count.
- After sorting, the code copies the sorted values into an `ArrayList<Integer>` because the method returns an `ArrayList`.

Why this is good for beginners:
- It shows how to use a custom comparator for sort order.
- It uses Java's built-in bit counting helper `Integer.bitCount`.
- It clearly separates conversion, sorting, and output creation.

## Key takeaways for beginners

- The problem is not about numeric value order, but about the number of `1` bits in binary form.
- All solutions count bits first, then sort by that count.
- Python uses a sort key directly.
- C++ uses bucket grouping with `__builtin_popcount`.
- Java uses `Integer.bitCount` and a comparator.
- Descending order means more set bits appear earlier in the output.

Understanding this problem helps build two useful skills:
- working with binary representations
- using custom sorting logic in different languages
