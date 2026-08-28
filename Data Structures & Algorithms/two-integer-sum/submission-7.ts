class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    // {5: [0, 1]}
    twoSum(nums: number[], target: number): number[] {
        const hashmap = {};

        // object with number as key, index of number as value
        for (let i = 0; i < nums.length; i++) {
            const number = nums[i];
            hashmap[number] = hashmap[number] ? [...hashmap[number], i] : [i];
        }

        for (const num of nums) {
            const diff = target - num;
            const indexOfDiff = hashmap[diff];
            if (!indexOfDiff) continue;

            const indexOfNum = hashmap[num];
        

            if (diff === num) {
                if (indexOfNum.length > 1) return [indexOfNum[0], indexOfNum[1]]
                continue
                }

            return [indexOfNum[0], indexOfDiff[0]]


            // if the other number is in hash map then cool
        }
    }
}
