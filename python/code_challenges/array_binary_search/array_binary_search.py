import math

def BinarySearch(arr,x):
    """
    algoriyhme to insert list,x and search using Binary Search and retrive the index value for were we found x inside the array
    input=>[10,20,30,40,50], 20)
    2
    """
    firstElement=0
    lastelement=len(arr)-1

    while(firstElement<=lastelement):
         midElement=math.ceil((firstElement+lastelement)/2)
         if arr[midElement]==x:
             return midElement
         else:
             if x<arr[midElement]:
                 lastelement=midElement-1
             else:
                 firstElement=midElement+1
    return -1

# print(BinarySearch([11, 22, 33, 44, 55, 66, 77], 90))
print (BinarySearch([10,20,30,40,50], 20))
# print (BinarySearch([4,8,15,16,23, 42], 15))
# print (BinarySearch([-131, -82, 0, 27, 42, 68, 179], 42))
# print(BinarySearch([1, 2, 3, 5, 6, 7], 4))








