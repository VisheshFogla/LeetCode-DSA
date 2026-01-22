class Solution:
    def reverseBits(self, n: int) -> int:
        num = format(n, '032b')
        rev = ''.join(reversed(num))

        return int(rev, 2)