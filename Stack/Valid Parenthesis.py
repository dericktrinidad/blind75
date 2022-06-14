class Solution:
    def isValid(self, s):
        parentheses = {
            '{' : '}',
            '(' : ')',
            '[' : ']',
        }
        stack = []
        for c in s:
            if c in parentheses:
                if stack and stack[-1] == parentheses[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            return True if not stack else False
if __name__ == '__main__':
    s = Solution()
    print(s.isValid("(]){adfg}d[asdf]"))

