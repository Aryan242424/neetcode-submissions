class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lst1 = [char for char in s]
        lst2 = [char for char in t]
        lst1.sort()
        lst2.sort()
        return lst1 == lst2
        