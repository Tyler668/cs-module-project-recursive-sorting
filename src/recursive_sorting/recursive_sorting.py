# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB, arr):

    i = 0
    j = 0
    k = 0

    # Your code here
    while i < len(arrA) and j < len(arrB):
        if arrA[i] <= arrB[j]:
            arr[k] = arrA[i]
            i+=1
        elif arrB[j] < arrA[i]:
            arr[k] = arrB[j]
            j+=1
        k+=1
    while i < len(arrA):
        arr[k] = arrA[i]
        k+=1
        i+=1
    while j < len(arrB):
        arr[k] = arrB[j]
        k+=1
        j+=1



# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    n = len(arr)
    
    if n < 2:
        return arr

    mid = n//2
    left = [0] * mid
    right = [0] * (n - mid) 

    for i in range(len(left)):
        left[i] = arr[i]

    for i in range(len(right)):
        right[i] = arr[mid + i]

    merge_sort(left)
    merge_sort(right)
    merge(left, right, arr)

    return(arr)


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end): 
    

    
    start2 = mid + 1 
  
    # If the direct merge is already sorted 
    if (arr[mid] <= arr[start2]): 
        return arr
      
    # Two pointers to maintain start 
    # of both arrays to merge 
    while (start <= mid and start2 <= end): 
  
        # If element 1 is in right place 
        if (arr[start] <= arr[start2]): 
            start += 1 
        else: 
            value = arr[start2]
            index = start2 
  
            # Shift all the elements between element 1 
            # element 2, right by 1. 
            while (index != start): 
                arr[index] = arr[index - 1] 
                index -= 1 
              
            arr[start] = value
  
            # Update all the pointers 
            start += 1
            mid += 1
            start2 += 1 




def merge_sort_in_place(arr, l, r): 

    if len(arr) < 2:
        return arr    

    if (l < r): 
  
        # Same as (l + r) / 2, but avoids overflow 
        # for large l and r 
        m = l + (r - l) // 2
  
        # Sort first and second halves 
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)
  
        merge_in_place(arr, l, m, r)

        return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr


print(merge_sort([1,14,4,30,6,8,3,5,9,3,11,8,4,3]))