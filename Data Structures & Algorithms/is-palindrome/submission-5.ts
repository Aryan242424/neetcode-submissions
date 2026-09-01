class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s: string): boolean {
        let cleanString = ''
        for (const char of s) {
            if (this.isAlphaNumeric(char)) {
                cleanString += char.toLowerCase()

            }
        }

        return [...cleanString].reverse().join('') === cleanString
    }

    isAlphaNumeric(char: string) {
        return (char >= 'a' && char <= 'z') || (char >= 'A' && char <= 'Z') || (char >= '0' && char <= '9')

    }
}
