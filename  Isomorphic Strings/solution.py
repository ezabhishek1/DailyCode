class Solution:
    def areIsomorphic(self, s1, s2):
        # ═══════════════════════════════════════════════════════════════
        # APPROACH: Two-Way Bijective Mapping
        # ═══════════════════════════════════════════════════════════════
        # 
        # Two strings are isomorphic if there exists a one-to-one (bijective)
        # character mapping between them.
        # 
        # Do we need TWO mappings?
        # 
        # Example: s1 = "ba", s2 = "aa"
        #   - Forward map: b→a, a→a (seems valid)
        #   - But 'b' AND 'a' both map to 'a' (NOT one-to-one!)
        # 
        # Solution: Keep BOTH forward and reverse mappings:
        #   - Forward: s1 char → s2 char
        #   - Reverse: s2 char → s1 char
        # 
        # This ensures:
        #   1. Each s1 character maps to exactly one s2 character
        #   2. Each s2 character is mapped from exactly one s1 character
        # ═══════════════════════════════════════════════════════════════
        
        d = {}        # Forward mapping: s1 → s2
        rev_d = {}    # Reverse mapping: s2 → s1
        
        for a, b in zip(s1, s2):
            # Check forward mapping
            if a in d:
                if d[a] != b:
                    return False  # Same s1 char maps to different s2 chars
            else:
                # Create forward mapping
                d[a] = b
                
                # Check reverse mapping
                if b in rev_d:
                    if rev_d[b] != a:
                        return False  # Different s1 chars map to same s2 char
                else:
                    # Create reverse mapping
                    rev_d[b] = a
        
        return True


# ═══════════════════════════════════════════════════════════════
# COMPLEXITY ANALYSIS
# ═══════════════════════════════════════════════════════════════
# 
# Time Complexity: O(n)
#   - Single pass through both strings
#   - Dictionary operations: O(1) average case
#   - Total: O(n) where n is the length of the strings
# 
# Space Complexity: O(1) for lowercase letters, O(k) in general
#   - Forward dict: at most min(n, alphabet_size) entries
#   - Reverse dict: at most min(n, alphabet_size) entries
#   - For lowercase English (26 chars): effectively O(1)
#   - For general case with alphabet size k: O(k)
# 
# ═══════════════════════════════════════════════════════════════
# 
# DRY RUN Example:
# 
# s1 = "egg", s2 = "add"
# 
# Step 1 (a='e', b='a'):
#   - 'e' not in d, so d['e'] = 'a'
#   - 'a' not in rev_d, so rev_d['a'] = 'e'
#   - State: d={e:a}, rev_d={a:e}
# 
# Step 2 (a='g', b='d'):
#   - 'g' not in d, so d['g'] = 'd'
#   - 'd' not in rev_d, so rev_d['d'] = 'g'
#   - State: d={e:a, g:d}, rev_d={a:e, d:g}
# 
# Step 3 (a='g', b='d'):
#   - 'g' in d and d['g'] == 'd' ✓
#   - (No reverse map creation needed, already exists)
#   - State: unchanged
# 
# Result: True ✓
# 
# ═══════════════════════════════════════════════════════════════