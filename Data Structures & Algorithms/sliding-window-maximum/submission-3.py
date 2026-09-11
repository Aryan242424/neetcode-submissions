class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        q = deque()

        l = 0
        for r in range(len(nums)):

            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            window_length = r + 1 - l

            if window_length == k:
                if q[0] < l: 
                    q.popleft()
                result.append(nums[q[0]])
   
                l += 1
        return result
                
            

            
        