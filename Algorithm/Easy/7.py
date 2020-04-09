'''
7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: 
[−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''


class Solution:
    def reverse(self, x):

        sign = [1, -1][x < 0] #sign = 1 if x > 0 else -1
        x *= sign
        rev = 0
        
        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10 #x = int(x / 10)
        
        rev = sign * rev
            
        if rev < -0x7fffffff or rev > 0x7fffffff-1: #0x7fffffff=2^31
            return 0
        return rev
