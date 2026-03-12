class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        count = 0

        for i in range (0, len(details)):
            if (int(details[i][11:13])) > 60:
                count = count + 1
        
        return count
            