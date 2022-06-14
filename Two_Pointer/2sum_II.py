class Solution:
    def twosumII(self, nums, target):
        l, r = 0 , len(nums) - 1
        while r > l:
            sum = nums[l] + nums[r]
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []





if __name__ == '__main__':
    s = Solution()
    print(s.twosumII([1,3,4,5,7,11], 9))