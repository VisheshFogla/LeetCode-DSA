class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        total = 0

        for i in range (0, len(operations)):
            if operations[i] == 'C':
                total = total - result[len(result) - 1]
                result.remove(result[len(result) - 1])
            elif operations[i] == 'D':
                total = total + result[len(result) - 1] * 2
                result.append(result[len(result) - 1] * 2)
            elif operations[i] == '+':
                total = total + result[len(result) - 1] + result[len(result) - 2]
                result.append(result[len(result) - 1] + result[len(result) - 2])
            else:
                total = total + int(operations[i])
                result.append(int(operations[i]))
                
        return total



