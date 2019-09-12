#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
Description: 剑指offer第一题目：二维数组查找

Authors: gengmingjin(gengmingjin@bupt.edu.cn)
Date: 2019/09/12 14:38:44
"""


import os

class Solution(object):
    """ solution"""
    def badfind(self, target, array):
        """
        查找某个数字是否在二维数组中(bad)
        Args:
            target: 待查找的目标数字
            array: 查找范围
        Return:
             True/False
        """
        # 暴力查找/根本没有利用行和列都是递增这一条件
        for i in range(len(array)):
            for j in range(len(array[0])):
                if target == array[i][j]:
                    return True
        return False

    def goodfind(self, target, array):
        """
        查找某个数字是否在二维数组中(good)
        Args:
            target: 待查找目标数字
            array: 查找范围
        Return:
            True/False
        """
        # 从某一角开始比较,然后指针向两个方向移动
        if target is None or array is None:
            return False
        i = len(array) - 1
        j = 0             # 从左下角开始进行
        while i >= 0 and j < len(array[0]):
            if array[i][j] == target:
                print(i, j)
                return True
            elif array[i][j] < target:
                j += 1
            elif array[i][j] > target:
                i -= 1
        return False

if __name__ == "__main__":
    #  the array here is :  1  2  3  4
    #                       3  5  6  8
    #                       4  7  8  9
    #                       5  10 11 12
    array = [[1, 2, 3, 4], [3, 5, 6, 8], [4, 7, 8, 9], [5, 10, 11, 12]]
    target = 12
    print(array)
    solve = Solution()
    print(solve.badfind(target, array))
    print(solve.goodfind(target, array))