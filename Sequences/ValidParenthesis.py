class Solution:
    def isValid(self, s):
        stack = []
        dict_bracket = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        for c in s:
            if c in dict_bracket:
                if stack and stack[-1] == dict_bracket[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

if __name__ == '__main__':
    s = Solution()
    print(s.isValid("()[]{}"))