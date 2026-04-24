class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1

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
        
        l1 = 0
        r1 = left 

        m1 = (l1 + r1) // 2

        l2 = right
        r2  = len(nums) - 1

        m2 = (l2 + r2) // 2 

        while (l1 <= r1):

            if nums[m1] < target:
                l1 = m1 + 1
                m1 = (l1 + r1) // 2
            elif nums[m1] > target: 
                r1 = m1 - 1
                m1 = (l1 + r1) // 2
            else: 
                return m1
        
        
        while (l2 <= r2):
            if nums[m2] < target:
                l2 = m2 + 1
                m2 = (l2 + r2) // 2
            elif nums[m2] > target: 
                r2 = m2 - 1
                m2 = (l2 + r2) // 2
            else: 
                return m2

        return -1
            
