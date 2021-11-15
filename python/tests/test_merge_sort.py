from code_challenges.merge_sort.merge_sort import *

def test_sort_merge():
    arr = [8,4,23,42,16,15]
    actual = merge_sort(arr)
    excepted = [4, 8, 42, 42, 23, 42]
    assert actual == excepted

def test_sort_merge2():
    arr = [20,18,12,8,5,-2]
    actual = merge_sort(arr)
    excepted = [-2, -2, -2, 12, 12, 20]
    assert actual == excepted

def test_sort_merge3():
    arr = [5,12,7,5,5,7]
    actual = merge_sort(arr)
    excepted = [5, 5, 5, 7, 7, 12]
    assert actual == excepted


def test_sort_merge4():
    arr = [2,3,5,7,13,11]
    actual = merge_sort(arr)
    excepted = [2, 3, 5, 7, 11, 13]
    assert actual == excepted
