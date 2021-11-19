def quick_sort(arr,left,right):
    """
    check if left < right
    call partition
    recall quick_sort with (arr, left, position-1)
    recall quick_sort with (arr, position+1, right)
    """
    if left < right:
        position = partition(arr, left, right)
        quick_sort (arr, left, position-1)
        quick_sort (arr, position+1, right)
    return arr


def partition(arr, left ,right):
    """
    set pivot right value in array
    loop where i > left and less than right
    if value less than pivot call swap function
    """
    pivot = arr[right]
    low = left-1
    for i in range(left,right):
        if arr[i]<= pivot:
            low +=1
            swap(arr, i, low)

    swap(arr, right, low+1)
    return low+1

def swap(arr,i,low):
    """
    to swap between value in the array
    """
    temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp

if __name__=="__main__":
    arr = [8,4,23,42,16,15]
    len_arr = len(arr)
    len_arr = len_arr-1
    print (quick_sort(arr, 0, len_arr),"unsorted array")
    #====================================
    arr = [20,18,12,8,5,-2]
    len_arr = len(arr)
    len_arr = len_arr-1
    print (quick_sort(arr, 0, len_arr),"Reverse-sorted")
    #====================================
    arr = [5,12,7,5,5,7]
    len_arr = len(arr)
    len_arr = len_arr-1
    print (quick_sort(arr, 0, len_arr),"Few_uniques")
    #====================================
    arr = [2,3,5,7,13,11]
    len_arr = len(arr)
    len_arr = len_arr-1
    print (quick_sort(arr, 0, len_arr),"Nearly-sorted")




