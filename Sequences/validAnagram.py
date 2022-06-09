class Solution:
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)

if __name__ == '__main__':
    s = Solution()
    print(s.isAnagram("anagram", "nagaram"))