class ValidParenthesis:
    def isValid(self, s):
        stack = []
        m = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in m:
                top_element = stack.pop() if stack else '#'
                if m[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack
v=input()
print(ValidParenthesis().isValid(v))