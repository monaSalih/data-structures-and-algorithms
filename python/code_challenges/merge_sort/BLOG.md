## Merge sort
 It works on the principle of Divide and Conquer. Merge sort repeatedly breaks down a list into several sublists until each sublist consists of a single element and merging those sublists in a manner that results into a sorted list
----
 ## Pseudo Code

```

ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```
----
## Trace
This algorithme is divide and sort unsorted array
```
        [ 20 ,18  ,12  ,8  ,5  ,-2]

[20, 18, 12]                    [8,  5,  -2]

[18, 20]   [12]                  [8,5] [-2]

[18, 20] [12]                   [5, 8] [-2]

[18,20, 12]                        [5,8,-2]

[12,18, 20]                       [-2,8,5]


           [-2, 8, 5, 12,18,20]
```
