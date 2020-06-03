
arr = [0, 1, 3, 6, 100, 101, 900]


def bin_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        #   determine mid point of array
        mid = (left + right) // 2
        # if we find target return the mid
        if arr[mid] == target:
            return mid
        #   if target is less than current value change right to mid - 1
        # elimnating all elements from mid to right from our search
        elif target < arr[mid]:
            right = mid - 1

# if target is > than curr value elimnate all elements from begining of arr
# to the mid point
        else:
            left = mid + 1

    return -1


# print(bin_search(arr,6)) #3
print(bin_search(arr, 0))  # 5
print('<><><>')
print(bin_search(arr, 900))  # 6
