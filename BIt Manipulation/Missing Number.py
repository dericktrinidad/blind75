class Solution:
    def missingNumber(self, nums):
        res = len(nums)

        for i in range(len(nums)):
            res += (i - nums[i])
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.missingNumber([9,6,4,2,3,5,7,0,1]))


