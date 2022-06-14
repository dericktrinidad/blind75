class Solution:
    def threesum(self, nums):
        sums = []
        nums.sort()
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            else:
                l, r = i + 1, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r] + n
                    if s < 0:
                        l += 1
                    elif s > 0:
                        r -= 1
                    else:
                        sums.append([nums[l], nums[r], n])
                        #only need to shift one pointer after solution found
                        l += 1
                        # if left pointer is same as prev left pointer and left less than right: keep shifting leftpointer
                        while nums[l] == nums[l - 1] and l < r:
                            l += 1
        return sums


if __name__ == '__main__':
    s = Solution()
    print(s.threesum([-1,0,1,2,-1,-4]))