class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        if len(nums) == 1:
            if target == nums[0]:
                return True
            else:
                return False

        left = 0
        right = len(nums) - 1

        mid = (left + right) // 2

        if nums[left] != nums[right]:
            while(right - left != 1):
            
                if nums[mid] >= nums[left]: 
                    left = mid
                    mid = (left + right) // 2
            
                elif nums[mid] <= nums[left]:
                    right = mid
                    mid = (left + right) // 2
        else: 
            for i in range(1, len(nums)):
                if(nums[i] < nums[i-1]):
                    left = i - 1
                    right = i
                    break


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
                return True
        
        
        while (l2 <= r2):
            if nums[m2] < target:
                l2 = m2 + 1
                m2 = (l2 + r2) // 2
            elif nums[m2] > target: 
                r2 = m2 - 1
                m2 = (l2 + r2) // 2
            else: 
                return True

        return False
            
