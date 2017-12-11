# Binary search algorithms

def binary_search(arr, item):
    low = 0
    high = len(arr)

    while low <= high:
        mid = low + (high - low) / 2

        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            low = mid + 1
        else:
            high = mid - 1

    return Exception("Item not found")


# needs to be fixed
def recursive_binary_search(arr = None, low = 0, high = -1, item = None):

    mid = low + (high - low) / 2
    

    if arr[mid] == item:
        return mid
    elif arr[mid] < item:
        return recursive_binary_search(arr, mid + 1, high, item)
    else:
        return recursive_binary_search(arr, low, mid - 1, item)

    return Exception("Item not found")


my_arr = [1, 3, 5, 7, 8, 11, 15, 1229]

print binary_search(my_arr, 1229)
print recursive_binary_search(my_arr, 0, len(my_arr), 15)
