class Solution {
    // Helper function to calculate Greatest Common Divisor
    private int gcd(int a, int b) {
        if (b == 0) return a;
        return gcd(b, a % b);
    }

    // Simulation function: pours water from one jug to another
    private int solve(int fromCap, int toCap, int target) {
        int fromJug = 0;
        int toJug = 0;
        int steps = 0;

        while (fromJug != target && toJug != target) {
            // Fill the 'from' jug if it's empty
            if (fromJug == 0) {
                fromJug = fromCap;
                steps++;
            }

            // Pour from 'fromJug' to 'toJug'
            int transfer = Math.min(fromJug, toCap - toJug);
            toJug += transfer;
            fromJug -= transfer;
            steps++;

            // Check if target is reached after pouring
            if (fromJug == target || toJug == target) {
                break;
            }

            // Empty the 'to' jug if it's full
            if (toJug == toCap) {
                toJug = 0;
                steps++;
            }
        }

        return steps;
    }

    public int minSteps(int m, int n, int d) {
        // Edge case: target is 0
        if (d == 0) return 0;
        
        // Edge case: target is exactly one of the jug capacities
        if (d == m || d == n) return 1;

        // Check if a solution is possible:
        // 1. Target cannot exceed the capacity of the larger jug
        // 2. Target must be a multiple of the GCD of both jugs
        if (d > Math.max(m, n) || d % gcd(m, n) != 0) {
            return -1;
        }

        // Return the minimum steps between starting with Jug M or starting with Jug N
        return Math.min(solve(m, n, d), solve(n, m, d));
    }
}