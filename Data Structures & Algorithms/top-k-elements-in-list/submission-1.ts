class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums: number[], k: number): number[] {
        const map = new Map<number, number>()

        for (const num of nums) {
            const value = (map.get(num) ?? 0 ) + 1
            map.set(num, value)
        }
        // 0(n)

        // {1: 2 times, 2: 3 times, 4: 4 times}

        // k most frequent elements
        // max frequency of any number = n, ie the size of the    array
        const map2 = new Map<number, number[]>()
        for (let i = 0; i < nums.length; i++ ) {
            map2.set(i, [])
        }

        for (const [value, frequency] of map.entries()) {
            map2.set(frequency, [value, ...map2.get(frequency) ?? []])
        }

        let counter = nums.length
        let final: number[] = []

        while (final.length < k) {
            final = [...final, ...map2.get(counter) ?? []]
            counter = counter - 1

        } 

        return final


    }
}
