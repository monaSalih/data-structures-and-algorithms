## nsertion Sort:

Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.

##  Pseudocode
```
  InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp
```

## output step_by_step

**step_one**
input => [8,4,23,42,16,15]  min_num=4(swip between 8 and 4)
result => [4,8,23,42,16,15]

**step_two**
input => [4,8,23,42,16,15]   min_num=8
result => [4,8,23,42,16,15]

**step_three**
input => [4,8,23,42,16,15]   min_num=16 (swip between 16 and 42)
input => [4,8,23,16,42,15]  min_num=16 (swip between 16 and 23)
result => [4,8,16,23,42,15]

**step_four**
input => [4,8,16,23,42,15]  min_num=15 (swip between 15 and 42)
input => [4,8,16,23,15,42]  min_num=15 (swip between 15 and 23)
input => [4,8,16,15,23,42]  min_num=15 (swip between 15 and 16)
result => [4,8,15,16,23,42]
