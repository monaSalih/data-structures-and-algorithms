def merge_sort(arr):
    n = len (arr)

    if n > 1:
        mid = n//2
        left = arr [0:mid]
        right = arr [mid:]

        merge_sort(left)
        merge_sort(right)
        merge(left,right,arr)

    return arr

def merge (left,right,arr):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i = i+1
        else:
            arr[k] = right[i]
            j = j+1
        k = k+1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

if __name__ == "__main__":
    test_arr = [8,4,23,42,16,15]
    print (merge_sort(test_arr))

    Reverse_sorted = [20,18,12,8,5,-2]
    print (merge_sort(Reverse_sorted))

    Few_uniques = [5,12,7,5,5,7]
    print (merge_sort(Few_uniques))

    Nearly_sorted = [2,3,5,7,13,11]
    print (merge_sort(Nearly_sorted))

