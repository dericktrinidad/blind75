class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while (l <= r):
            mid = (r + l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid-2
            elif nums[mid] < target:
                l = mid + 1
        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.search([-1,0,3,5,9,12], 9))