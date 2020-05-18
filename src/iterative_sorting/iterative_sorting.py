# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # first select the smallest value and move to position 0
    # move next smallest value to position 1
    # repeat
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(cur_index+1, len(arr)):
            if arr[j] <= arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        # Your code here
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Starting with the first element(index = 0), compare the current element with the next element of the array.
    # If the current element is greater than the next element of the array, swap them.
    # If the current element is less than the next element, move to the next element. Repeat Step 1.
    # Your code here
    size = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for j in range(0, size-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here

    return arr
