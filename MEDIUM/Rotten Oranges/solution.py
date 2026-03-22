from collections import deque

class Solution:
    def orangesRot(self, mat):
        rows, cols = len(mat), len(mat[0])
        q = deque()
        fresh = 0
        
        # Step 1: Initialize queue with rotten oranges
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 2:
                    q.append((r, c, 0))  # (row, col, time)
                elif mat[r][c] == 1:
                    fresh += 1
        
        # Step 2: BFS
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        time = 0
        
        while q:
            r, c, t = q.popleft()
            time = max(time, t)
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == 1:
                    mat[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc, t + 1))

        return -1 if fresh > 0 else time