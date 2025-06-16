class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:


        result = []

        if len(nums) == 0: 

            return result

        start = nums[0]
        end = nums[0]

        for i in range (0, len(nums) - 1):   

            if nums[i + 1] is not None:
                if nums[i] + 1 != nums[i + 1]: 
                    if start == end:
                        result.append(str(start))
                    else:
                        result.append(str(start) + "->" + str(end))
                    
                    start = nums[i + 1]
                    end = nums[i + 1]
                else:
                    end = nums[i + 1]

        if start == end:
            result.append(str(start))
        else:
            result.append(str(start) + "->" + str(end))

        return result



                 
            
            