class Solution:
    def groupAnagram(self, strs):
        Anagram_dict = {}
        for s in strs:
            sorted_string = ''.join(sorted(s))
            if sorted_string not in Anagram_dict:
                Anagram_dict[sorted_string] = [s]
            else:
                Anagram_dict[sorted_string].append(s)
        return list(Anagram_dict.values())

if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagram(["eat","tea","tan","ate","nat","bat"]))