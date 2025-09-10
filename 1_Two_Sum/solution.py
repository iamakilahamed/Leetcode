class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Solution 1
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         sum = 0
        #         if i != j:
        #             sum = nums[i] + nums[j]
        #             if sum == target:
        #                 return [i, j]

        # Solution 2
        # numMap = {}
        # for i in range(len(nums)):
        #     numMap[nums[i]] = i
        # for i in range(len(nums)):
        #     complement = target - nums[i]
        #     if complement in numMap and numMap[complement] != i:
        #         return [i, numMap[complement]]            
        # return []
    
        # Solution 3
        numMap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i
        return []