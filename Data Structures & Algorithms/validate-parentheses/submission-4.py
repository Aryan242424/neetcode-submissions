class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in bracket_map.values(): #opening 
                stack.append(char)
            elif not stack or stack.pop() != bracket_map[char]: # closing added to empty stack
                return False
    
    
        
        return len(stack) == 0


            

            


        