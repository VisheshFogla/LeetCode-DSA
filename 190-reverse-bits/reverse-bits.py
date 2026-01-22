class Solution:
    def reverseBits(self, n: int) -> int:
        num = format(n, '032b')

        print(num)

        rev = ''.join(reversed(num))

        print(rev)

        return int(rev, 2)