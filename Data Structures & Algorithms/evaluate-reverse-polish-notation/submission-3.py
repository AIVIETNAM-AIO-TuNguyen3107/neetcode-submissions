class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                num = stack.pop()
                prev_num = stack.pop()
                if token == "+":
                    current_result = num + prev_num
                elif token == "*":
                    current_result = num * prev_num
                elif token == "-":
                    current_result = prev_num - num
                elif token == "/":
                    current_result = int(prev_num / num)
                stack.append(current_result)
            else:
                stack.append(int(token))
        return stack[0]
