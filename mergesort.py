# Merges two subarrays of arr[]
# First subarray is arr[l..m]
# Second subarray is arr[m+l...r]
def merge(array, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    #create temp arrays
    temparr1 = [0] * (n1)
    temparr2 = [0] * (n2)

    #copy data to temp arrays temparr1[] and temparr2[]
    for i in range(0, n1):
        temparr1[i]= array[l+i]

    for j in range(0, n2):
        temparr2[j] = array[m+1+j]

    #Merge the temp arrays back into arr[l..r]
    i = 0  #initial index of first subarray
    j = 0  #initial index of second subarray
    k = l  #initial index of merged subarray

    while(i<n1 and j<n2):
        if temparr1[i] <= temparr2[j]:
            array[k] = temparr1[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1

    #Copy the remaining elements of temparr1[] , if there
    # are any
    while i < n1:
        array[k] = temparr1[i]
        i += 1
        k += 1

    #Copy the remaining elements of temparr2[] , if there are any
    while j < n2:
        array[k] = temparr2[j]
        j += 1
        k += 1

# l is for left index and r is right index of the
# sub-array of arr to br sorted

def mergesort(arr, l, r):
    if l < r:
        #same as (l+r)/2, but avoids overflow for
        # large l and h
        m = (l+(r-1))/2

        #sort first and second halves
        mergesort(arr, l, m)
        mergesort(arr, m+1, r)
        merge(arr, l, m, r)




