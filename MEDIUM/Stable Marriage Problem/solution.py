class Solution:
    def stableMarriage(self, men, women):
        n = len(men)
        
        # Step 1: Create ranking matrix for women
        rank = [[0]*n for _ in range(n)]
        for w in range(n):
            for i in range(n):
                rank[w][women[w][i]] = i
        
        # Step 2: Initialize
        free_men = list(range(n))
        next_proposal = [0] * n
        woman_partner = [-1] * n
        result = [-1] * n
        
        # Step 3: Process until all men are matched
        while free_men:
            m = free_men.pop(0)
            
            w = men[m][next_proposal[m]]
            next_proposal[m] += 1
            
            if woman_partner[w] == -1:
                # Woman is free
                woman_partner[w] = m
                result[m] = w
            else:
                current = woman_partner[w]
                
                # Check preference
                if rank[w][m] < rank[w][current]:
                    # She prefers new man
                    woman_partner[w] = m
                    result[m] = w
                    result[current] = -1
                    free_men.append(current)
                else:
                    # She rejects new man
                    free_men.append(m)
        
        return result