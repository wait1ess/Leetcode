class Solution:
    def convertToBase7(self, num: int) -> str:
        if num < 0: return '-' + self.convertTo7(-num)
        if num < 7: return str(num)
        return self.convertTo7(num // 7) + str(num % 7)
    def convertTo7(self, num):
        if num == 0: return '0'
        n, res = abs(num), ''
        while n:
            res = str(n % 7) + res
            n //= 7
        return res if num > 0 else '-' + res
