def largestElem(arr):
    largest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest        



print(largestElem([5,4,6,9,2,11]))
