class Solution:
    def productExceptSelf(self,nums):
        output = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        return output

if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([1,2,3,4]))