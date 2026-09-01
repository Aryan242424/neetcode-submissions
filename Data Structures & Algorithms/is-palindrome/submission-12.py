class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        # last comparison
        while left != len(s) - 1 and right != 0:
            # both are
            if (s[left].isalnum() and s[right].isalnum()):
                if (s[left].lower() != s[right].lower()):
                    return False
                left +=1
                right -=1 
                continue

            if not s[left].isalnum():
                left += 1

            if not s[right].isalnum():
                right -= 1

        return True
   

