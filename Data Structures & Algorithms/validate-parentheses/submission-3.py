class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        for char in s:
            if not stack: 
                stack.append(char)
                continue

            if char in bracket_map.values(): #opening 
                stack.append(char)
                continue
            
            # if closing 
            last_item = stack.pop()
            if last_item != bracket_map[char]:
                stack.append(last_item)
                stack.append(char)
        
        return len(stack) == 0


            

            


        