class Solution(object):
    def getSum(self, a, b):
        MAX = 0XFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        while b!=0:
            carry = ( a & b ) << 1
            a = (a ^ b) & MAX
            b= carry & MAX

        return a if a <= MAX_INT else ~(a ^ MAX)







        