class Solution:
    def containsDuplicate(self, nums):
        mem = {}
        bool = False
        if len(nums) == 1:
            return False
        for i, value in enumerate(nums):
            if value in mem:
                return True
            else:
                bool = False
                mem[value] = i
        return bool

if __name__ == '__main__':
    s = Solution()
    print(s.containsDuplicate([0,4,5,0,3,6]))
