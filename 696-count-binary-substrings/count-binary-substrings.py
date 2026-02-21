class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        count = 0

        if len(s) == 1:
            return count

        a = 0 
        b = 0
        count = 0

        flag = False

        for i in range (0, len(s)):
            
            if s[i] != '1': 
                if flag == True: 
                    a = 0
                    a = a + 1
                    flag = False
                else: 
                    a = a + 1

            if s[i] != '0':
                if flag == False:
                    b = 0
                    b = b + 1
                    flag = True
                else: 
                    b = b + 1
            
            if flag == True and a != 0:
                count = count + 1
                a = a - 1

            if flag == False and b != 0:
                count = count + 1
                b = b - 1

        return count

            

            
                