# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 21:16:55 2018

@author: rocky
"""

"""
回文数判断
Determine whether an integer is a palindrome.
 An integer is a palindrome when it reads the same backward as forward.
 input 121 output True
 input 123 output False
"""

class Solution:
    def isPalindrome(self,x):
        if x<0:
            return False
        summ,copy=x,0
        while summ:
            copy=copy*10+summ%10
            summ=summ//10
        return copy==x
if __name__=='__main__':
    print(Solution().isPalindrome(67876))