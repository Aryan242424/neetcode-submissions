class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        highest_pile = min_speed = max(piles)
        potential_valid = range(1, highest_pile + 1)
        l, r = 0, len(potential_valid) -1

        while r >= l:
            m = l + (r -l ) // 2
            eating_speed = potential_valid[m]
            
            num_hours = 0
            for pile in piles:
                num_hours += math.ceil(pile / eating_speed)
            if num_hours > h:
                l = m + 1
            else: # valid found try smaller
                min_speed = min(min_speed, eating_speed)
                r = m - 1
                   
        
        return min_speed