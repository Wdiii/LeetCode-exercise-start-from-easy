# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def convertToTitle(self, n: int) -> str:
        res=""
        while n!=0:
            res=chr((n-1)%26+65)+res
            n=(n-1)//26
        return res
