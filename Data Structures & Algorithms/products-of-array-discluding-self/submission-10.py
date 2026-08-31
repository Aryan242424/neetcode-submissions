class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1st pass
        prefix_array = [1] * (len(nums))
        prefix_accumulator = 1

        for i, num in enumerate(nums):
            prefix_array[i] = prefix_accumulator
            prefix_accumulator *= num

        # second pass
        postfix_array = [1] * (len(nums))
        postfix_accumulator = 1

        for i in range(len(nums) - 1, -1, -1):
            postfix_array[i] = postfix_accumulator
            postfix_accumulator *= nums[i]

        final = []
        for i in range(len(nums)):
            final.append(prefix_array[i] * postfix_array[i])
        return final




        





        