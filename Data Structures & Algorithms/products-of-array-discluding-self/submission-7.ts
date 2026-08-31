class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums: number[]): number[] {
        // guarantee that this is a positive number
        let product = 1
        let zeroCount = 0
        const final = []

        // first loop
        for (const num of nums) {
            if (num == 0) {
                zeroCount++
                continue
            }
            product = product * num
        }

        for (const num of nums) {
            if (zeroCount > 1) {
                final.push(0)
                continue
            }
            // zero count is 1 or less

            if (zeroCount === 1) {
                final.push(num === 0 ? product : 0)
                continue
            }
            
            final.push(product / num)

            
        }

        return final

    }

}
