class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums: number[]): number {
        const numSet = new Set(nums)
        let longest = 0

        for (const num of nums) {
            if (!numSet.has(num - 1)) {
                let counter = 1 // one seen so far

                while (numSet.has(num + counter)) {
                    counter ++
                }

                longest = Math.max(longest, counter)



            }
        }
        return longest
    }
}
