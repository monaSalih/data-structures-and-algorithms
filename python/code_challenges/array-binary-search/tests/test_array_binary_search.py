from array_binary_search import __version__
from array_binary_search.array_binary_search import BinarySearch


def test_version():
    assert __version__ == '0.1.0'



def test_BinarySearch():
    #inputs arr ,number to insert it
    arr=[11, 22, 33, 44, 55, 66, 77]
    x=90

    #output
    newArr=-1
    assert BinarySearch(arr,x)==newArr

def test_BinarySearch2():
    #inputs arr ,number to insert it
    arr=[10,20,30,40,50]
    x=20

    #output
    newArr=1
    assert BinarySearch(arr,x)==newArr


def test_BinarySearch3():
    #inputs arr ,number to insert it
    arr=[4,8,15,16,23, 42]
    x=15

    #output
    newArr=2
    assert BinarySearch(arr,x)==newArr


def test_BinarySearch4():
    #inputs arr ,number to insert it
    arr=[-131, -82, 0, 27, 42, 68, 179]
    x=42

    #output
    newArr=4
    assert BinarySearch(arr,x)==newArr
