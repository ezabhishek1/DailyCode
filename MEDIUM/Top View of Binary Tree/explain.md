🔎 Hint 1: Think in terms of horizontal distance (HD)
- Assign the root node HD = 0.
- For every left child, HD = parent’s HD – 1.
- For every right child, HD = parent’s HD + 1.
- The top view is simply the first node you encounter at each HD.

🔎 Hint 2: Use BFS (level-order traversal)
- If you traverse level by level, the first time you see a node at a given HD, it’s guaranteed to be the topmost one.
- Store it in a map keyed by HD.

🔎 Hint 3: Sorting the result
- After traversal, you’ll have a map from HD → node value.
- To print from leftmost to rightmost, sort the keys (HDs) and collect values in order.


# Some BUGGY QUESTIONS: 

1. Why can't I use DFS instead of BFS?! It works well too, does it not?
Answer: 
- Yes, you can use DFS, but it will make your code a bit trickier, and it may give you wrong results!
- DFS can go deep and overwrite nodes at the same HD, which breaks the “topmost” rule.
- BFS naturally ensures shallow nodes are processed first.