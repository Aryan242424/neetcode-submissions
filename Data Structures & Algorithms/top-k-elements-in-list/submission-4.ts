class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums: number[], k: number): number[] {
        const freq = new Map<number, number>()
        for (const num of nums) {
            freq.set(num, (freq.get(num) ?? 0) + 1)
        }

        const numList: number[][] = Array.from({length: nums.length + 1}, () => [])

        // nested array done

        for (const [num, frequency] of freq.entries()) {
            numList[frequency].push(num)
        }

        let i = nums.length
        const final: number[] = []
        while (final.length < k) {
            final.push(...numList[i])
            i = i - 1
        }

        return final






    }
}
