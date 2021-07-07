# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(A, B):
    # init the combined list that will hold the sorted elements from both A and B
    # combined = [0] * (len(A) + len(B))
    # combined = [0 for _ in range(len(A) + len(B))]
    combined = []

    # init the two pointers that start at each list 
    a = 0
    b = 0

    while a < len(A) and b < len(B):
        # compare the elements that a and b point at 
        if A[a] < B[b]:
            combined.append(A[a])
            a += 1
        else:
            combined.append(B[b])
            b += 1

    # at this point, we've finished traversing one of the lists completely
    # we need to add all of the elements from the other list to the combined list 
    while a < len(A):
        combined.append(A[a])
        a += 1 
    while b < len(B):
        combined.append(B[b])
        b += 1

    return combined


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # break the array down recursively
    # base case: when the lists get down to lengths of 1 
    if len(arr) > 1:
        left = merge_sort(arr[:len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        arr = merge(left, right)
    
    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m 

    L = [0] * (n1) 
    R = [0] * (n2) 
  
    # Copy data to temp arrays L[] and R[] 
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
  
    # Merge the temp arrays back into arr[l..r] 
    i = 0     # Initial index of first subarray 
    j = 0     # Initial index of second subarray 
    k = l     # Initial index of merged subarray 
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
  
    # Copy the remaining elements of L[], if there 
    # are any 
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    # Copy the remaining elements of R[], if there 
    # are any 
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1


def merge_sort_in_place(arr,l,r): 
    if l < r: 
  
        # Same as (l+r)//2, but avoids overflow for 
        # large l and h 
        m = (l+(r-1))//2
  
        # Sort first and second halves 
        merge_sort_in_place(arr, l, m) 
        merge_sort_in_place(arr, m+1, r) 
        merge_in_place(arr, l, m, r) 


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr