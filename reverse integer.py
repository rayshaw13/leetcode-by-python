# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 21:04:19 2018

@author: rocky
"""

"""
reverse integer
Given a 32-bit signed integer, reverse digits of an integer.
input 123 output 321

Assume we are dealing with an environment
 which could only store integers within the 32-bit signed integer range: [−2**31,  2**31 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

class Solution:
    def reverse(self,x):
        xx=abs(x)
        sign=1 if x>0 else -1
        summ=0
        while xx:
            summ=summ*10+xx%10
            xx=xx//10
        if summ<=0x7fffffff:
            return sign*summ
        else:
            return 0
if __name__=='__main__':
    print(Solution().reverse(125))