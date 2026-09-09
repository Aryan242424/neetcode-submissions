class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = defaultdict(int)
        for char in t:
            t_map[char] += 1
        
        #move forward until u find the first char that appears in t
        need = len(t_map)
        min_length = float('inf')
        substring = [0, 0]
        s_map = defaultdict(int)
        have = 0

        l = 0
        for r in range(len(s)):
            char = s[r]
            s_map[char] += 1

            if char in t_map and s_map[char] == t_map[char]:
                have += 1

            while have == need:
                str_len = r + 1 - l
                if str_len < min_length:
                    substring = [l, r + 1]
                    min_length = str_len
                
                s_map[s[l]] -= 1
                

                if s[l] in t_map and s_map[s[l]] < t_map[s[l]]: 
                    have -= 1

                l += 1

        return s[substring[0]: substring[1]] if min_length != float('inf') else ""



                    





        