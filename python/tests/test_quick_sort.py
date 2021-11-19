from code_challenges.quick_sort.quick_sort import *


def test_quick_sort1():
    arr = [8,4,23,42,16,15]
    len_arr = len(arr)
    len_arr = len_arr-1
    actuall = quick_sort(arr, 0, len_arr)
    excepted = [4, 8, 15, 16, 23, 42]
    assert actuall == excepted

def test_quick_sort2():
    arr = [20,18,12,8,5,-2]
    len_arr = len(arr)
    len_arr = len_arr-1
    actuall = quick_sort(arr, 0, len_arr)
    excepted = [-2, 5, 8, 12, 18, 20]
    assert actuall == excepted

def test_quick_sort3():
    arr = [5,12,7,5,5,7]
    len_arr = len(arr)
    len_arr = len_arr-1
    actuall = quick_sort(arr, 0, len_arr)
    excepted = [5, 5, 5, 7, 7, 12]
    assert actuall == excepted

def test_quick_sort4():
    arr = [2,3,5,7,13,11]
    len_arr = len(arr)
    len_arr = len_arr-1
    actuall = quick_sort(arr, 0, len_arr)
    excepted = [2, 3, 5, 7, 11, 13] 
    assert actuall == excepted
