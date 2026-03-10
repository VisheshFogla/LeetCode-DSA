class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        arr = []

        for i in range(2* len(nums)):

            if i >= len(nums):
                i = i - len(nums)

            arr.append(nums[i])

        return arr