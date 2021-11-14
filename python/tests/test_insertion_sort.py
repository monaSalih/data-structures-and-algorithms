from code_challenges.Insertion_sort.Insertion_sort import *

#input_array
def test_input_array():
    assert insertion_sort([8,4,23,42,16,15])==[4, 8, 15, 16, 23, 42]
#reverse_sorted
def test_reverse_sorted():
    assert insertion_sort([20,18,12,8,5,-2])==[-2, 5, 8, 12, 18, 20]

# Few_uniques
def test_few_uniques():
    assert insertion_sort([5,12,7,5,5,7])==[5, 5, 5, 7, 7, 12]

#Nearly_sorted
def test_nearly_sorted():
    assert insertion_sort([2,3,5,7,13,11])==[2, 3, 5, 7, 11, 13]
