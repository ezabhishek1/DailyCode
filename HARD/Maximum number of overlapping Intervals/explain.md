# Maximum Number of Overlapping Intervals

## Problem Statement
Given an array of intervals, find the **maximum number of intervals that overlap at any point in time**.

An interval `[s, e]` overlaps with another interval if they share at least one common point.

## Why the Naive Approach Fails

### ❌ Naive Approach: O(n²) - TLE
```
For each interval:
    For each other interval:
        Check if they overlap
        Count overlaps
```
This approach requires comparing every pair of intervals, resulting in **O(n²)** time complexity, which causes **Time Limit Exceeded (TLE)**.

### ✅ Optimized Approach: Event-Based Sweep Line - O(n log n)
Instead of checking pairwise overlaps, we use an **event-based approach**:

**Key Insight:** At any point in time, the number of overlapping intervals equals the number of **"start" events** minus the number of **"end" events** we've encountered so far.

## Solution Strategy

### The Sweep Line Algorithm

#### Step 1: Create Events (Not 2*n Array Sorting)
Rather than creating a 2D array of all intervals and sorting them (which is inefficient), we create **separate events** for incoming and leaving intervals:

```
For each interval [s, e]:
    - Create START event: (s, +1)      // Interval starts
    - Create END event:   (e+1, -1)    // Interval ends (add 1 because intervals are inclusive)
```

**Why `e+1` instead of `e`?**
- If one interval ends at time `e` and another starts at time `e`, they overlap
- We mark the end as `e+1` so that when we process events at the same timestamp, we process all starts before the ends

#### Step 2: Sort Events by Timestamp
Sort all events by their timestamp (start time). This is **O(n log n)** and much more efficient than sorting intervals.

#### Step 3: Sweep Through Events
Process events in chronological order and track:
- **`curr`**: Current number of overlapping intervals at this point
- **`best`**: Maximum overlapping intervals seen so far

**For events at the same timestamp:**
- Process all events with the same timestamp together
- This handles ties correctly

#### Step 4: Return Maximum
Return the maximum count observed during the sweep.

## Pseudo Code
```
function maxOverlappingIntervals(intervals):
    events = []
    
    // Create events
    for each interval [s, e] in intervals:
        events.append((s, +1))
        events.append((e+1, -1))
    
    // Sort events by timestamp
    sort events
    
    // Sweep through events
    curr = 0
    best = 0
    i = 0
    
    while i < length(events):
        x = events[i].timestamp
        delta = 0
        
        // Process all events at same timestamp
        while i < length(events) and events[i].timestamp == x:
            delta += events[i].value
            i += 1
        
        curr += delta
        best = max(best, curr)
    
    return best
```

## Example Walkthrough

### Input
```
intervals = [[1, 3], [2, 4], [5, 6], [1, 2]]
```

### Step 1: Create Events
| Interval | Start Event | End Event |
|----------|------------|-----------|
| [1, 3]   | (1, +1)    | (4, -1)   |
| [2, 4]   | (2, +1)    | (5, -1)   |
| [5, 6]   | (5, +1)    | (7, -1)   |
| [1, 2]   | (1, +1)    | (3, -1)   |

### Step 2: Sort Events
```
Sorted events: [(1, +1), (1, +1), (2, +1), (3, -1), (4, -1), (5, -1), (5, +1), (7, -1)]
```

### Step 3: Sweep Through Events

| Timestamp | Events | Delta | Current | Best |
|-----------|--------|-------|---------|------|
| 1         | +1, +1 | +2    | 2       | 2    |
| 2         | +1     | +1    | 3       | **3** |
| 3         | -1     | -1    | 2       | 3    |
| 4         | -1     | -1    | 1       | 3    |
| 5         | -1, +1 | 0     | 1       | 3    |
| 7         | -1     | -1    | 0       | 3    |

### Output
```
Maximum overlapping intervals = 3
```
At time `t=2`, intervals `[1,3]`, `[2,4]`, and `[1,2]` overlap.

## Why This Works

✓ **Events with same timestamp handled together:** Processes all starts and ends at time `t` atomically  
✓ **End marked as `e+1`:** Correctly handles adjacent intervals  
✓ **Single pass after sorting:** Efficient O(n) sweep after O(n log n) sort  
✓ **No redundant comparisons:** Only tracks active intervals, not pairwise comparisons  

## Complexity Analysis

| Metric | Value | Explanation |
|--------|-------|-------------|
| **Time Complexity** | O(n log n) | O(n) to create events + O(n log n) to sort + O(n) to sweep |
| **Space Complexity** | O(n) | Store 2n events |

## Key Takeaways

- **Separate incoming and leaving events** instead of sorting a 2D array of intervals
- **Event-based approach** reduces complexity from O(n²) to O(n log n)
- **Process same-timestamp events together** to avoid missing overlaps
- **Mark interval end as `e+1`** to correctly handle inclusive intervals
- This pattern is useful for many interval-based problems (meeting rooms, calendar scheduling, etc.)
