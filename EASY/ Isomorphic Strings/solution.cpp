class Solution {
  public:
    bool areIsomorphic(string &s1, string &s2) {
        // ═══════════════════════════════════════════════════════════════
        // APPROACH: Two-Way Bijective Mapping using Arrays
        // ═══════════════════════════════════════════════════════════════
        // 
        // For lowercase English letters (a-z), use arrays instead of maps
        // for O(1) constant-time access without hashing overhead.
        // 
        // hash1[i]: character 'a'+i from s1 maps to which character in s2
        // hash2[i]: character 'a'+i from s2 maps to which character in s1
        // 
        // Both mappings must be consistent.
        // ═══════════════════════════════════════════════════════════════
        
        vector<int> hash1(26, -1);  // s1 char → s2 char mapping
        vector<int> hash2(26, -1);  // s2 char → s1 char mapping
        int n = s1.size();
        
        for(int i = 0; i < n; i++){
            char ch1 = s1[i];
            char ch2 = s2[i];
            
            // Convert to indices (0-25 for a-z)
            int need1 = ch1 - 'a';
            int need2 = ch2 - 'a';
            
            // Check if ch1 already has a mapping
            if(hash1[need1] != -1){
                // Verify it maps to the same ch2
                if(hash1[need1] != need2) 
                    return false;
            }
            // Check if ch2 already has a reverse mapping
            else if(hash2[need2] != -1){
                // Verify it maps back to the same ch1
                if(hash2[need2] != need1) 
                    return false;
            }
            // Both are new, create bidirectional mappings
            else {
                hash1[need1] = need2;
                hash2[need2] = need1;
            }
        }
        
        return true;
    }
};

/*
═══════════════════════════════════════════════════════════════
COMPLEXITY ANALYSIS
═══════════════════════════════════════════════════════════════

Time Complexity: O(n)
  - Single pass through both strings
  - Array access: O(1)
  - Total: O(n) where n is the length of the strings

Space Complexity: O(1)
  - hash1: fixed size of 26 (for a-z)
  - hash2: fixed size of 26 (for a-z)
  - Total: O(26) = O(1) constant space
  
  Note: This is more space-efficient than using HashMaps
  for bounded character sets.

═══════════════════════════════════════════════════════════════

Why Two Mappings?

Consider: s1 = "ba", s2 = "aa"

With only hash1 forward mapping:
  - b → a, a → a (looks valid)
  - Problem: Both 'b' and 'a' map to 'a'!

With both mappings:
  - hash1: b→a, a→a
  - hash2: a→b? But we already have a→a (CONFLICT!)
  - Result: False ✓

═══════════════════════════════════════════════════════════════

DRY RUN Example:

s1 = "egg", s2 = "add"

i=0: ch1='e'(4), ch2='a'(0)
  - hash1[4] == -1, hash2[0] == -1
  - Create: hash1[4]=0, hash2[0]=4

i=1: ch1='g'(6), ch2='d'(3)
  - hash1[6] == -1, hash2[3] == -1
  - Create: hash1[6]=3, hash2[3]=6

i=2: ch1='g'(6), ch2='d'(3)
  - hash1[6] == 3 ✓ (matches ch2=3)
  - Continue

Result: true ✓

═══════════════════════════════════════════════════════════════
*/