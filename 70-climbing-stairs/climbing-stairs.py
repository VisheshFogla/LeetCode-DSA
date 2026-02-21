class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1: 
            return 1
        
        if n == 2:
            return 2

        a = 2
        count = 3

        for i in range (3, n + 1):
            
            if i == n:
                return count
            else:
                temp = count
                count = a + count
                a  = temp
        
                