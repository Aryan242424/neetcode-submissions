class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board: string[][]): boolean {
        const cols = new Map<number, Set<String>>()
        const rows = new Map<number, Set<String>>()
        const squares = new Map<string, Set<String>>()


        for (let row = 0; row < 9; row ++) {
            for (let col = 0; col < 9; col++) {
                const value = board[row][col]
                const key = `${Math.floor(row/3)}:${Math.floor(col/3)}`
                
                if (!cols.get(col)) cols.set(col, new Set())
                if (!rows.get(row)) rows.set(row, new Set())
                if (!squares.get(key)) squares.set(key, new Set())

                if (value === ".") continue
                if (cols.get(col).has(value) || rows.get(row).has(value) ||                 squares.get(key).has(value))
                return false

                cols.get(col).add(value)
                rows.get(row).add(value)
                squares.get(key).add(value)



            }
        }

        return true

    }
}
