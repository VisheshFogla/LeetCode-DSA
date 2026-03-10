class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        arr = []

        for i in range(len(nums)):

            arr.insert(i, nums[i])
            arr.insert(len(nums) + i, nums[i])

        return arr