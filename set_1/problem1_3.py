#python 2.7.3

# -*- coding:utf-8 -*-

class MaxGap:
    def findMaxGap(self, A, n):
        ma = max(A)
        return abs(ma-min(A[0],A[n-1]))
        # write code here