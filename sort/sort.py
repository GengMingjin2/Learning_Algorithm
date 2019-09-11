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
    T:O(n^2) S:O(1)
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
    T:O(nlogn) S:O(logn)
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
    T:O(n^2) S:O(1)
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
    T:O(nlogn) S:O(1)
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

def select_sort(inlst, decs=False):
    """
    The select sort method in python.(unstable)
    T:O(n^2) S:O(1)
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
    for i in range(0, n - 1):
        min_index = i
        for j in range(i + 1, n):
            if inlst[j] < inlst[min_index]:
                min_index = j
        if min_index != i:
            inlst[i], inlst[min_index] = inlst[min_index], inlst[i]
    if decs:
        inlst.reverse()
    return inlst

def heap_sort(inlst, decs=False):
    """
    The heap sort method in python.(unstable)
    T:O(nlogn) S:O(1)
    Args:
        inlst: The number list to be sorted.
        decs: A flag to decide the output order.
              True: large -> small
              False: small -> large
    Return:
        outlst: The sorted number list.
    """
    def heap_adjust(tmplst, start, end):
        """
        Adjust the heap generated from tmplst.
        Args:
            tmplst: A list to adjust
            start: the root of the heap
            end: the last leaf node of the heap in tmplst
        Return:
        """
        temp = tmplst[start]
        child = 2 * start + 1   # the left child of the start~
        while child <= end:
            if child < end and tmplst[child] < tmplst[child + 1]:
                child += 1
            if temp >= tmplst[child]:  # check whether the heap is a big-roof heap~
                break
            tmplst[start] = tmplst[child]
            start = child
            child = 2 * child + 1
        tmplst[start] = temp # !!!

    n = len(inlst)
    if n <= 1:
        return inlst
    root = n // 2 - 1 # the last non-leaf node in the heap
    while(root >= 0):
        heap_adjust(inlst, root, n - 1)
        root -= 1
    i = n - 1
    while(i >= 0):
        inlst[0], inlst[i] = inlst[i], inlst[0] # exchange the last node in the heap with the root node.
        heap_adjust(inlst, 0, i - 1)
        i -= 1
    if decs:
        inlst.reverse()
    return inlst

def merge_sort(inlst, decs=False):
    """
    The merge sort method in python.(stable)
    T:O(nlogn) S:O(n)
    Args:
        inlst: The number list to be sorted.
        decs: A flag to decide the output order.
              True: large -> small
              False: small -> large
    Return:
        outlst: The sorted number list.
    """
    def merge(tmplst, left, mid, right):
        """
        Merge the two sub-array
        Args:
            tmplst:  a list
            left: the start index for the left sub-array
            mid: the middle of the tmplst
            right: the end index for the right sub-array
        Return:
        """
        temp = []
        i = left
        j = mid + 1
        while i <= mid and j <= right:
            if tmplst[i] <= tmplst[j]:
                temp.append(tmplst[i])
                i += 1
            else:
                temp.append(tmplst[j])
                j += 1
        while i <= mid:
            temp.append(tmplst[i])
            i += 1
        while j <= right:
            temp.append(tmplst[j])
            j += 1
        for i in range(left, right + 1):
            tmplst[i] = temp[i - left]

    def msort(tmplst, left, right):
        """
        Merge Function
        Args:
            tmplst: a list
            left: the left index
            right: the right index
        Return:
        """
        if left >= right:
            return
        mid = (left + right) // 2
        msort(tmplst, left, mid)
        msort(tmplst, mid + 1, right)
        merge(tmplst, left, mid, right)

    n = len(inlst)
    if n <= 1:
        return inlst
    msort(inlst, 0, n - 1)
    if decs:
        inlst.reverse()
    return inlst

if __name__ == "__main__":
    out = read_keyboard()
    print("bubble_sort results: ", bubble_sort(out))
    print("quick_sort results: ", quick_sort(out))
    print("insert_sort results: ", insert_sort(out))
    print("shell_sort results: ", shell_sort(out))
    print("select_sort results: ", select_sort(out))
    print("heap_sort results: ", heap_sort(out))
    print("merge_sort restuls: ", merge_sort(out))