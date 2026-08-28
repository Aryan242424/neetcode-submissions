class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # general trick  - anagrams = same when sorted
        # any order

        dict = {}
        for i, string in enumerate(strs):
            char_list = [char for char in string]
            char_list.sort()

            char_tuple = tuple(char_list)
            if char_tuple not in dict:
                dict[char_tuple] = [i]
            else:
                dict[char_tuple].append(i)

        lst = []
        for key in dict:  # we get an array here
            sublist = []
            for i in dict[key]:
                sublist.append(strs[i])
            lst.append(sublist)

        return lst
