class Solution:
    def groupAnagrams(self, strs):
        mem = {}
        for i, s in enumerate(strs):
            if "".join(sorted(s)) in mem:
                mem["".join(sorted(s)) ].append(s)
            else:
                mem["".join(sorted(s)) ] = [s]
        return mem.values()
if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
