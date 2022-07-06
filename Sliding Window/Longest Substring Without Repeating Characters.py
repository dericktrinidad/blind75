class Solution:
    def lengthOfLongestSubstring(self, s):
        charSet = set()
        l = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

    def lengthOfLongestSubstring2(self, s):
        HashSet = set()
        for i in s:
            if i not in HashSet:
                HashSet.add(i)
            else:
                while HashSet.pop() != i:
                    HashSet.pop()
                HashSet.add(i)
        return HashSet
if __name__ == '__main__':
    s = Solution()
    # print(s.lengthOfLongestSubstring("dvdf"))
    print(s.lengthOfLongestSubstring2("dvdf"))