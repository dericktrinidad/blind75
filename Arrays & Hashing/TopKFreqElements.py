class Solution:
    def topKFrequent(self, nums, k):
        nums_dict = {}
        solution = []
        for i in set(nums):
            nums_dict[i] = nums.count(i)
        # print(dict(sorted(nums_dict.items(), key=lambda item: item[1], reverse=True)))
        TopFrequent = list(dict(sorted(nums_dict.items(), key=lambda item: item[1], reverse=True)))
        for j in range(k):
            solution.append(TopFrequent[j])
        return solution

if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([1,1,1,1,2,2,2,3,3,5],3))