class Solution:
    def containsDuplicate(self, nums):
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
if __name__ == '__main__':
    s = Solution()
    print(s.containsDuplicate([0,4,5,0,3,6]))
