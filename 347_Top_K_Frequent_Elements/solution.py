class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        my_dict = {}
        for num in nums:
            if num not in my_dict:
                my_dict[num] = 1
            else:
                my_dict[num] = my_dict.get(num) + 1
        my_dict = dict(sorted(my_dict.items(), key = lambda item: item[1], reverse = True))
        result = list(my_dict.keys())[:k]
        return result