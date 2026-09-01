class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #naive solution attempt
        res = []
        nums.sort() # nlogn time

        for i, v in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            target = -v
            if i >= len(nums) - 1: continue

            two_sums = self.twoSum(nums, target, i + 1) 
            if not two_sums: continue # skip

            triplets = [i + [v] for i in two_sums]

            res.extend(triplets)
    
        return res


    def twoSum(self, nums: List[int], target: int, start_index: int) -> List[List[int]]:
        l = start_index
        r = len(nums) - 1
        res = []
    
        
        while l < r: # sorted lst btw
            sum = nums[l] + nums[r]
            if (sum == target): 
                res.append([nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1] : l +=1
                while l < r and nums[r] == nums[r + 1] : r -=1
            elif (sum > target): r -=1
            else: l +=1
        return res


        




        