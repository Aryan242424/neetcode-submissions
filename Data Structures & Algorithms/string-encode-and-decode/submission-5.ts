class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs: string[]): string {
        let encoded = ""
        for (const str of strs) {
            const length = String(str.length)
            encoded += length+"#" + str
        }
        return encoded
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str: string): string[] {
        const decoded = []
        let nextIndex = 0

        while (nextIndex < str.length) {
            let endIndex = nextIndex

            while (str[endIndex] !== "#") {
                endIndex++
            }

            const length = Number(str.slice(nextIndex, endIndex))
            const start = endIndex + 1
            const end = start + length
            decoded.push(str.slice(start, end))
            nextIndex = end

        }
        return decoded

    }
}
