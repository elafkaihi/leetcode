class Solution:
    def isValid(self, s: str) -> bool:
        mapy = {")":"(", "]":"[", "}":"{"}
        stack = []
        for c in s : 
            if c not in mapy:
                stack.append(c)
                continue
            if not stack or stack[-1] != mapy[c]:
                return False
        return len(stack) == 0 