class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        valid_parentheses_pair = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        stack = []
        for c in s:
            if stack:
                if stack[-1] not in valid_parentheses_pair: return False
                elif valid_parentheses_pair[stack[-1]] == c:
                    stack.pop()
                elif c in valid_parentheses_pair:
                    stack.append(c)
                else:
                    return False
            else:
                stack.append(c)
        return True if len(stack) == 0 else False