class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_map_s1 = defaultdict(int)
        for char in s1:
            freq_map_s1[char] +=1
        
        freq_map_s2 = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            window_length = r - l + 1
            char = s2[r]
            freq_map_s2[char] += 1

            if window_length == len(s1):
                if freq_map_s1 == freq_map_s2:
                    return True
                else:
                    freq_map_s2[s2[l]] -= 1
                    if freq_map_s2[s2[l]] == 0:
                        del freq_map_s2[s2[l]]
                    l += 1
            
        return False



     


            

            
