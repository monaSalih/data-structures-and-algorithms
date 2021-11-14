def insertion_sort(arr):
    len_arr = len (arr)
    for i in range (1,len_arr):
        j = i-1
        temp = arr[i]
        while j>=0 and temp < arr[j]:
            arr [j+1] = arr[j]
            j = j-1

        arr [j+1] =temp
    return arr

if __name__ == "__main__":
    input_array = [8,4,23,42,16,15]
    Reverse_sorted = [20,18,12,8,5,-2]
    Few_uniques = [5,12,7,5,5,7]
    Nearly_sorted = [2,3,5,7,13,11]
    print(insertion_sort(input_array))
    print(insertion_sort(Reverse_sorted))
    print(insertion_sort(Few_uniques))
    print(insertion_sort(Nearly_sorted))

