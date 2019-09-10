#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Description: Different sorting methods.(Python Version)

Authors: gengmingjin(gengmingjin@bupt.edu.cn)
Date: 2019/09/10 17:12:32
"""
import os

def read_keyboard():
    """
    Read from the keyboard inputs and return a list.
    Example:
        input: 1 2 3 4 5
        returns: [1,2,3,4,5]( a list )
    """
    input_str = input("Please input the numbers: ")
    output_lst = input_str.split(" ")
    try:
        for i in range(len(output_lst)):
            try:
                output_lst[i] = int(output_lst[i])
            except:
                print("Invalid input!")
        return output_lst
    except:
        print("No input from keyboard!")

def bubble_sort(inlst, decs=False):
    """
    The bubble sort method in python.(stable)
    Args:
        inlst: The number list to be sorted.
        decs: A flag to decide the output order.
             True: large -> small
             False: small -> large
    Return:
        outlst: The sorted number list.
    """
    n = len(inlst)
    if n <= 1:
        return inlst
    if_exchange = False
    for i in range(0, n):  # 遍历的次数
        for j in range(0, n - i - 1):  # 单次遍历内比较的次数
            if inlst[j] > inlst[j + 1]:
                inlst[j], inlst[j + 1] = inlst[j + 1], inlst[j]
                if_exchange = True
        if not if_exchange:
            break
    if decs:
        inlst.reverse()
    return inlst

def quick_sort(inlst, decs=False):
    """
    The quick sort method in python.(unstable)
    Args:
        inlst: The number list to be sorted.
        decs: A flag to decide the output order.
              True: large -> small
              False: small -> large
    Return:
        outlst: The sorted number list.
    """
    def partition(tmplst, left, right):
        """
        The partition function.
        Args:
            tmplst: the input list to be divided
            left: the left index of the tmplst
            right: the right index of the tmplst
        Return:
            left: the index of the partition
        """
        key = left
        while left < right:
            while left < right and tmplst[right] >= tmplst[key]:
                right -= 1
            while left < right and tmplst[left] <= tmplst[key]:
                left += 1
            tmplst[left], tmplst[right] = tmplst[right], tmplst[left]
        tmplst[left], tmplst[key] = tmplst[key], tmplst[left]
        return left

    def qsort(tmplst, left, right):
        """
        Recurrently Sorting.
        Args:
            tmplst: the input list to be sorted.
            left: the left index of the tmplst.
            right: the right index of the tmplst.
        """
        if left >= right:
            return
        mid = partition(tmplst, left, right)
        qsort(tmplst, left, mid - 1)
        qsort(tmplst, mid + 1, right)

    # main function
    n = len(inlst)
    if n <= 1:
        return inlst
    qsort(inlst, 0, n - 1)
    if decs:
        inlst.reverse()
    return inlst

def insert_sort(inlst, decs=False):
    """
    The insert sort method in python.(stable)
    Args:
        inlst: The number list to be sorted.
        decs: A flag to decide the output order.
              True: large -> small
              False: small -> large
    Return:
        outlst: The sorted number list.
    """
    n = len(inlst)
    if n <= 1:
        return inlst
    for i in range(1, n):
        j = i
        target = inlst[i]
        while j > 0 and target < inlst[j - 1]:
            inlst[j] = inlst[j - 1]
            j = j - 1
        inlst[j] = target
    if decs:
        inlst.reverse()
    return inlst

def shell_sort(inlst, decs=False):
    """
    The shell sort method in python.(unstable)
    Args:
        inlst: The number list to be sorted.
        decs: A flag to decide the output order.
              True: large -> small
              False: small -> large
    Return:
        outlst: The sorted number list.
    """
    def shellinsert(tmplst, d):
        """
        shell insert function
        Args:
            tmplst: the input lst
            d: the distance between two elements
        """
        n = len(tmplst)
        for i in range(d, n):
            j = i - d
            temp  = tmplst[i]
            while(j >= 0 and tmplst[j] > temp):
                tmplst[j + d] = tmplst[j]
                j -= d
            if j != i - d:
                tmplst[j + d] = temp
    n = len(inlst)
    if n <= 1:
        return inlst
    d = n // 2
    while d >= 1:
        shellinsert(inlst, d)
        d = d // 2
    if decs:
        inlst.reverse()
    return inlst

if __name__ == "__main__":
    out = read_keyboard()
    print("bubble_sort results: ", bubble_sort(out))
    print("quick_sort results: ", quick_sort(out))
    print("insert_sort results: ", insert_sort(out))
    print("shell_sort results: ", shell_sort(out))