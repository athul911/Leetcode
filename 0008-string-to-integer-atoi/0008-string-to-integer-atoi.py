class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_INT = (2 ** 31) - 1
        MIN_INT = -2 ** 31
        negative = False
        digits = []
        value = 0
        s = s.strip()
        if s and s[0] == '-':
            negative = True
            s = s[1:]
        elif s and s[0] == '+':
            s = s[1:]
        if not s or not s[0].isnumeric():
            return 0
        for i in range(len(s)):
            if s[i].isnumeric():
                digits.append(s[i])
            elif digits:
                break

        value = int("".join(digits)) * -1 if negative else int("".join(digits))

        if value < MIN_INT:
            value = MIN_INT
        elif value > MAX_INT:
            value = MAX_INT
        return value