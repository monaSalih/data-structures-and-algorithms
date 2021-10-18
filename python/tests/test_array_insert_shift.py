from code_challenges.array_insert_shift.array_insert_shift import __version__
from code_challenges.array_insert_shift.array_insert_shift import insertShiftArray


def test_version():
    assert __version__ == '0.1.0'

# def test_array():
#     # input
#    array=[1,4,5,7]
#    p=-5
# #    output
#    outputArr =[1,4,-5,5,7]
# # assert
#    assert insertShiftArray(p,array) == outputArr


def test_insertShiftArrayTest():
    #inputs arr ,number to insert it
    arr=[2,4,6,-8]
    v=5
    #output
    newArr=[2,4,5,6,-8]
    assert insertShiftArray(arr,v)==newArr

def test_insertShiftArrayTest1():
    #inputs arr ,number to insert it
    arr=[42,8,15,23,42]
    v=16
    #output
    newArr=[42,8,15,16,23,42]
    assert insertShiftArray(arr,v)==newArr
