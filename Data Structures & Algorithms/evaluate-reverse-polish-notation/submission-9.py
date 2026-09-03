class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator_tokens = ['+', '-', '*', '/']

        stack = []

        for token in tokens:
            if token not in operator_tokens:
                stack.append(int(token))
                continue
            # you have encountered an operator with a non empty stack
            val2 = stack.pop()
            val1 = stack.pop()
            result = Solution.compute_result(token, val1, val2)
            stack.append(result)

        return stack.pop()

    @staticmethod
    def compute_result(operator: str, val1: int, val2: int):
        if operator == '+': return val1 + val2
        elif operator == '*': return val1 * val2
        elif operator == '-': return val1 - val2
        elif operator == '/': return int(val1 / val2)






                
                
                    

        