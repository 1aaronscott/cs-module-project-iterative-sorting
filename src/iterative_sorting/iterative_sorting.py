# TO-DO: Complete the selection_sort() function below
import random


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
    # count the occurences of each value in array and store in a temp array or dict
    # in the temp array add all the previous item counts making the values in this array cummulative
    # write the sorted values into the final array
    # Your code here
    #     count = [0]*len(set(arr))
    #     print(len(count))
    #     print(count)
    #     for value in arr:
    #         if value < 0:
    #             return "Error, negative numbers not allowed in Count Sort"
    #         count[arr.index(value)] += 1
    #     #     print(count)
    #     # for i in range(len(arr)-1):
    #     #     if arr[i] < 0:
    #     #         return "Error, negative numbers not allowed in Count Sort"
    #     #     count[i] += 1
    #     print(count)
    #     for j in range(1, len(count)):
    #         count[j] += count[j-1]

    # #    print(count)

    #     return arr

    #### Code from lecture ########
    if len(arr) == 0:  # O(1)
        return arr  # O(1)

    # if maximum is not given, we'll take the max value from the input array
    if maximum == -1:  # O(1)
        maximum = max(arr)  # O(n)

    # make a bunch of buckets
    buckets = [0 for _ in range(maximum+1)]  # O(max)

    for x in arr:  # O(n)
        if x < 0:
            return "Error, negative numbers not allowed in Count Sort"
        buckets[x] += 1  # O(1)

    # we have the counts of every value in our input array
    # loop through our buckets, starting at the smallest index
    # j keeps track of the spot we're writing to in our input array
    j = 0

    # this whole loop is reversing the tallying we did in the previous loop

    # max - n = diff
    for i in range(len(buckets)):  # O(max)
        while buckets[i] > 0:
            arr[j] = i
            j += 1
            buckets[i] -= 1

    return arr

    # arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
    # print(arr1)
    # count_sort(arr1)
    # arr3 = [1, 5, -2, 4, 3]
    # count_sort(arr3)
    #arr4 = random.sample(range(20), 50)


arr4 = random.choices(range(20), k=10)
print(arr4)
count_sort(arr4)
