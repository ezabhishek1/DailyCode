# Meeting Rooms - Attend All Meetings

## Problem Statement
Determine whether a person can attend all given meetings. A person can attend all meetings if there is no overlap between any two meetings.

## Key Insight
A person cannot attend two meetings if they overlap in time. The only valid condition is:
```
next_meeting.start >= previous_meeting.end
```

If `start < previous_end`, the meetings overlap and it's impossible to attend both.

## Solution Approach

### Algorithm Overview
The optimal solution leverages **sorting** to detect overlaps in O(n log n) time complexity:

1. **Sort meetings** by their start time
2. **Detect overlaps** by comparing adjacent meetings
3. **Return result** based on whether any overlap is found

### Step-by-Step Implementation

#### Step 1: Sort the Meetings
Sort the 2D array based on the **start time** of each meeting.

```
Input:  [[1,2], [7,10], [5,6], [2,3]]
After sorting: [[1,2], [2,3], [5,6], [7,10]]
```

**Why this works:** After sorting, if overlapping meetings exist, they will be adjacent to each other in the array.

#### Step 2: Traverse and Check for Overlaps
Iterate from the second meeting (index 1) onwards and compare each meeting with the previous one.

**Overlap condition:**
```
if (arr[i][0] < arr[i-1][1])
    → Current meeting starts before previous ends
    → Overlap detected
    → Return false
```

#### Step 3: Return Result
- If any overlap is found → return **false**
- If no overlaps exist after checking all meetings → return **true**

## Pseudo Code
```
function canAttendAllMeetings(meetings):
    if meetings.length <= 1:
        return true
    
    sort meetings by start time
    
    for i from 1 to meetings.length - 1:
        if meetings[i].start < meetings[i-1].end:
            return false  // Overlap found
    
    return true  // No overlaps
```

## Example Walkthrough

**Input:** `[[1,2], [7,10], [5,6], [2,3]]`

| Step | Description | Array State |
|------|-------------|-------------|
| 1 | Original array | `[[1,2], [7,10], [5,6], [2,3]]` |
| 2 | After sorting by start time | `[[1,2], [2,3], [5,6], [7,10]]` |
| 3 | Compare [2,3] with [1,2] | 2 ≥ 2 ✓ (No overlap) |
| 4 | Compare [5,6] with [2,3] | 5 ≥ 3 ✓ (No overlap) |
| 5 | Compare [7,10] with [5,6] | 7 ≥ 6 ✓ (No overlap) |
| **Result** | **No overlaps found** | **return true** |

### Counter Example
**Input:** `[[1,5], [2,4]]`

| Step | Description | Array State |
|------|-------------|-------------|
| 1 | Original array | `[[1,5], [2,4]]` |
| 2 | After sorting | `[[1,5], [2,4]]` |
| 3 | Compare [2,4] with [1,5] | 2 < 5 ✗ (Overlap!) |
| **Result** | **Overlap detected** | **return false** |

## Complexity Analysis

| Metric | Value | Explanation |
|--------|-------|-------------|
| **Time Complexity** | O(n log n) | Dominated by sorting; overlap check is O(n) |
| **Space Complexity** | O(1) or O(n) | Depends on sorting algorithm (in-place vs. not) |

## Key Takeaways
- ✓ Sorting enables efficient overlap detection
- ✓ Adjacent meetings in sorted order are the only ones that need comparison
- ✓ Time complexity is optimal for comparison-based approaches
- ✓ Works for any number of meetings