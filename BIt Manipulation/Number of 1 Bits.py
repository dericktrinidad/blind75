class Solution_shift:
    def hammingWeight(self, n):
        res = 0
        while n:
            res += (n % 2)
            n = n >> 1
        return res

class Solution_Most_Efficient:
    def hammingWeight(self, n):
        count = 0
        while n != 0:
            n = n & (n - 1)
            count += 1
        return count
if __name__ == '__main__':
    s = Solution_Most_Efficient()
    print(s.hammingWeight(1011))