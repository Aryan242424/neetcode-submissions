class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if k == len(s): return k

        max_len = k
        l = 0
        frequency = defaultdict(int)
        
        for r in range(len(s)):
            frequency[s[r]] += 1

            while (r + 1 - l) - (max(frequency.values())) > k:
                frequency[s[l]] -= 1
                l += 1
            # at this point substring len - most frequent <= k
            max_len = max(max_len, r - l + 1)
        return max_len


