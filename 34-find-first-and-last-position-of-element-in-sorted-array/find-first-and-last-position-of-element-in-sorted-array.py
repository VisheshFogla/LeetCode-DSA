class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        

        if len(nums) == 0:
            return [-1, -1]

        left = 0
        right = len(nums) - 1

        mid = (left + right) // 2
        found = None

        while (left <= right):

            if target > nums[mid]: 
                left = mid + 1
                mid = (left + right) // 2
            elif target < nums[mid]:
                right = mid - 1
                mid = (left + right) // 2
            else:
                found = mid
                break 

        
        if found == None: 
            return [-1, -1]
 
        left = 0
        r1 = found

        mid = (left + r1) // 2

        res = []

        if nums[left] != nums[r1]:
            while(r1 - left != 1):

                if target == nums[mid]:
                    r1 = mid 
                    mid = (left + r1) // 2
                elif target > nums[mid]:
                    left = mid
                    mid = (left + r1) // 2

            res.append(r1)
        else:
            res.append(left)
        
       

        left = found
        r2 = len(nums) - 1

        mid = (left + r2) // 2

        if nums[r2] != nums[left]:
            while(r2 - left != 1):
            
                if target == nums[mid]:
                    left = mid 
                    mid = (left + r2) // 2
                elif target < nums[mid]:
                    r2 = mid
                    mid = (left + r2)  // 2  

            res.append(left) 
        else:
            res.append(r2)

        
        return res