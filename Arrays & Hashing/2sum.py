class Solution():
    def twoSum(self, nums, target):
        mem = {}
        for i, val in enumerate(nums):
            diff = target - val
            if val in mem:
                return [mem[val], i]
            else:
                mem[diff] = i
if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))
