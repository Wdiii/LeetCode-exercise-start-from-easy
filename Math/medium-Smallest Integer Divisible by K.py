# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K%2==0 or K%5==0:
            return -1
        start=1
        while start%K!=0:
            start=start*10+1
        return len(str(start))