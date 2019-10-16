#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Description: 0-1 bag problem.

Author: gengmingjin(gengmingjin@bupt.edu.cn)
Date: 2019/10/16 11:32:17
"""

def bag(n, c, w, v):
    """
    Args:
        n: the number of the things.
        c: the total weight for the bag.
        w: the weight of every thing.(a list)
        v: the value of every thing.(a list)
    Return:
        the largest total value to select.
    """
    value = [[0 for j in range(c + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            value[i][j] = value[i - 1][j]
            if j >= w[i - 1] and value[i][j] < value[i - 1][j - w[i - 1]] + v[i - 1]:
                value[i][j] = value[i - 1][j - w[i - 1]] + v[i - 1]