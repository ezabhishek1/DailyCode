# Isomorphic Strings

## Problem Statement
Given two strings `s1` and `s2`, determine if they are **isomorphic**.

Two strings are isomorphic if:
- Each character in `s1` maps to **exactly one** character in `s2`
- Each character in `s2` is mapped to by **exactly one** character in `s1`
- The mapping preserves the order and pattern of characters

In other words, there must be a **bijective (one-to-one) correspondence** between characters.

### Examples
```
Input: s1 = "egg", s2 = "add"
Output: True
Mapping: e→a, g→d
Pattern: [1,2,2] → [1,2,2] ✓

Input: s1 = "badc", s2 = "baba"
Output: False
At position 2: 'd' should map to 'b', but 'd'→'a' from position 1
Also 'a' and 'b' both map to 'a' in reverse (violation)
```

## Core Idea

### Two-Way Mapping
The key insight is to maintain **two mappings**:
1. **Forward mapping**: s1 character → s2 character
2. **Reverse mapping**: s2 character → s1 character

Why both?
- Forward mapping ensures each s1 character maps to exactly one s2 character
- Reverse mapping ensures each s2 character is mapped from exactly one s1 character
- Together, they guarantee **bijection** (one-to-one correspondence)

### Algorithm Approach

1. **Simultaneous Mapping**: Iterate through both strings character by character
2. **Check Forward Mapping**: If s1[i] already exists in forward map:
   - Verify it maps to the same s2[i]
   - If not, return False (same s1 char maps to different s2 chars)
3. **Check Reverse Mapping**: If s2[i] already exists in reverse map:
   - Verify it maps back to the same s1[i]
   - If not, return False (different s1 chars map to same s2 char)
4. **Create New Mappings**: If both checks pass, create the bidirectional mapping

### Dry Run Example
```
s1 = "egg"
s2 = "add"

Index  s1[i]  s2[i]  Forward Map    Reverse Map    Valid?
  0     e      a     d[e]=a         rev_d[a]=e     ✓
  1     g      d     d[g]=d         rev_d[d]=g     ✓
  2     g      d     d[g]==d✓       rev_d[d]==g✓   ✓

Result: True

---

s1 = "badc"
s2 = "baba"

Index  s1[i]  s2[i]  Forward Map    Reverse Map    Check
  0     b      b     d[b]=b         rev_d[b]=b     ✓
  1     a      a     d[a]=a         rev_d[a]=a     ✓
  2     d      b     d[d]=b         rev_d[b]!=d✗   FAIL!
                                    rev_d[b]=b (from index 0)
                                    but we're trying to map 'd'

Result: False (different characters map to same character)
```

## Complexity Analysis

### Time Complexity: **O(n)**
- Single pass through both strings
- HashMap/Dictionary operations (insert, lookup): **O(1)** average case
- Total: **O(n)** where n is the length of the strings
- Must process every character once to verify isomorphism

### Space Complexity: **O(1)** or **O(k)** 
- **For lowercase English letters**: O(1) - at most 26 unique characters
- **For general case**: O(k) where k is the size of the character set
- Forward mapping stores at most k entries
- Reverse mapping stores at most k entries
- Total additional space: **O(k)**

**Important**: Space is constant for bounded character sets (like lowercase English letters).

## Use Cases

### 1. **Pattern Matching & String Similarity**
   - Fuzzy string matching in search engines
   - Finding similar word patterns in text
   - Spell checker pattern recognition
   - Detecting repeated character patterns in user input

### 2. **Data Validation & Format Checking**
   - Validating consistent variable naming patterns
   - Checking if password patterns are sufficiently different
   - Verifying consistent placeholder structures in templates
   - Validating data format consistency across records

### 3. **Text Encryption & Substitution Ciphers**
   - Validating substitution cipher consistency
   - Checking if encryption mapping is bijective
   - Detecting weak encryption patterns
   - Caesar cipher variant validation

### 4. **Biometric & Pattern Recognition**
   - Matching fingerprint patterns with templates
   - Validating consistent biological patterns
   - Analyzing gait recognition patterns
   - Iris/retina pattern matching

### 5. **Language Processing & NLP**
   - Identifying similar phonetic patterns across languages
   - Transliteration validation (e.g., converting Hindi to English)
   - Character encoding verification
   - Phoneme pattern matching

### 6. **Configuration & Environment Variables**
   - Validating consistent placeholder mapping in configuration files
   - Checking environment variable substitution patterns
   - Template rendering validation
   - Ensuring consistent naming conventions

### 7. **Database & Schema Mapping**
   - Validating column name mapping between tables
   - Checking field renaming consistency
   - Verifying data transformation consistency
   - Cross-database schema alignment

### 8. **Code Analysis & Refactoring**
   - Checking if variable renaming is consistent
   - Validating identifier mapping in code transformation
   - Detecting copy-paste errors with pattern variations
   - Code clone detection with pattern abstraction

### 9. **User Authentication**
   - Pattern lock validation (Android pattern lock)
   - Gesture recognition consistency
   - Sequential input pattern matching
   - Behavioral biometrics pattern validation

### 10. **Test Case Generation**
   - Generating equivalent test inputs
   - Creating pattern-preserving test cases
   - Validating normalization consistency
   - Creating isomorphic test data

## Algorithm Intuition

The elegance of checking isomorphism lies in the **bidirectional validation**:

1. **Why forward mapping alone isn't enough**:
   ```
   s1 = "ba", s2 = "aa"
   Forward only: b→a, a→a (looks valid)
   But 'b' and 'a' both map to 'a' (not bijective!)
   ```

2. **Why reverse mapping ensures one-to-one**:
   ```
   By tracking reverse mapping, we catch when multiple s1 characters
   try to map to the same s2 character.
   ```

3. **Checking both simultaneously**:
   ```
   Forward check: "Have I seen this s1 character before?"
   Reverse check: "Have I seen this s2 character before?"
   Only when both are new (or consistent) is it valid.
   ```

## Comparison: One Map vs Two Maps

| Approach | Correctness | Example Issue |
|----------|-------------|---------------|
| Single Forward Map | ❌ Incomplete | "ba" and "aa": both map to 'a' |
| Single Reverse Map | ❌ Incomplete | "aa" and "bc": 'a' maps from both 'b' and 'c' |
| **Both Maps** | ✅ **Complete** | Catches all violations of bijection |

## Implementation Variations

### Approach 1: Two Dictionaries (Python)
```python
d = {}        # s1 → s2
rev_d = {}    # s2 → s1
```
Most intuitive, clearly shows bidirectional mapping.

### Approach 2: Two Arrays (C++)
```cpp
vector<int> hash1(26, -1)  // s1[i] → s2[i]
vector<int> hash2(26, -1)  // s2[i] → s1[i]
```
More efficient for bounded character sets (lowercase letters).

### Approach 3: Single Data Structure
Some languages allow storing pairs or tuples, but two separate structures are clearer.

## Code Implementation Strategy

1. Initialize two empty mappings (dictionary/array)
2. Iterate through both strings simultaneously using zip or index
3. For each character pair (a, b):
   - Check forward: if a is mapped, verify it maps to b
   - Check reverse: if b is mapped, verify it maps to a
   - If either check fails, return False
   - Otherwise, create both mappings (a→b and b→a)
4. If loop completes without conflicts, return True

## Edge Cases

```
Empty strings: "" and "" → True (vacuously true)
Single character: "a" and "b" → True (trivial mapping)
Same string: "abc" and "abc" → True (identity mapping)
Repeated char: "aaa" and "bbb" → True (all map consistently)
Two-char conflict: "ba" and "aa" → False (both can't map to 'a')
```

## Optimization Notes

- **Early termination**: Return False as soon as a conflict is detected
- **Character set size**: For bounded sets (like a-z), space is O(1)
- **String length mismatch**: If lengths differ, isomorphism is impossible (can add early check)
- **Lazy evaluation**: Only compute mappings as needed

## Conclusion

Isomorphic strings require **bijective character mapping** - a perfect one-to-one correspondence. The two-way mapping approach elegantly ensures this property while maintaining O(n) time and O(1) space (for bounded character sets). This concept extends to pattern matching, encryption validation, and many real-world applications requiring structural equivalence.
