class Solution:
    def singleNumber(self, nums):
        ans = 0
        for i in nums:
            ans = i ^ ans

        return ans
if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([4,1,2,1,2]))