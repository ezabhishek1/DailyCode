# Approach
## Use a queue for BFS traversal.

## Keep track of each node’s horizontal distance (HD) from the root.

#### Root → HD = 0

#### Left child → HD - 1

#### Right child → HD + 1

## Store nodes in a map<int, vector<int>>, where the key is the HD.

## After traversal, extract values from the map (already sorted by HD).

## Return the collected columns as the final result.

# Complexity
 	 
## Time	O(Nlog⁡N)
## Space	O(N)
 