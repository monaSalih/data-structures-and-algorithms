# Challenge Summary
<!-- Description of the challenge -->
sort array using mearge sort, where take unsorted array and return it sorted using merge sorted
## Whiteboard Process
<!-- Embedded whiteboard image -->

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

## Solution
<!-- Show how to run your code, and examples of it in action -->

```
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
```


[pull_request]()
