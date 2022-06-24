class Solution:
    def longestConsecutive(self, nums):
        nums.sort()
        hashSet = set()
        l = 0
        for r in range(len(nums)):
            while nums[r] in hashSet:
                hashSet.remove(nums[l])
                l += 1
            hashSet.add(s[r])
            res = max(res)
            nums.remove
if __name__ == '__main__':
    s = Solution()
    print(s.longestConsecutive([100,4,200,1,3,2]))