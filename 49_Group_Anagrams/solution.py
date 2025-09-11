class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        my_dict = {}
        for word in strs:
            s = "".joined(sorted(word))
            if s in my_dict:
                my_dict[s].append(word)
            else:
                my_dict[s] = [word]
        result = list(my_dict.values())
        return result
