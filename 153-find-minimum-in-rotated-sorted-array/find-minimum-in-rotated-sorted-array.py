class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]


        left = 0
        right = len(nums) - 1

        mid = (left + right) // 2

        while(right - left != 1):


            if nums[mid] > nums[left]:
                left = mid
                mid = (left + right) // 2


            elif nums[mid] < nums[left]:
                right = mid
                mid = (left + right) // 2


        if nums[left] > nums[right]:
            return nums[right]
        else:
            return nums[0]

        
