class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        for t in s:
            if stack and t in brackets.keys():
                if stack.pop() != brackets[t]:
                    return False
            else:
                stack.append(t)
        return len(stack) == 0