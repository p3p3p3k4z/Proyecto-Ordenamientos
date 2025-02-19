import random
import heapq

def bubble_sort_characters(s):
    arr = list(s)
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertion_sort_characters(s):
    arr = list(s)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort_characters(s):
    arr = list(s)
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def merge_sort_characters(s):
    def merge(left, right):
        result = []
        while left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        while left:
            result.append(left.pop(0))
        while right:
            result.append(right.pop(0))
        return result
    
    arr = list(s)
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left_sorted = merge_sort_characters(arr[:mid])
        right_sorted = merge_sort_characters(arr[mid:])
        return merge(left_sorted, right_sorted)

def quick_sort_characters(s):
    arr = list(s)
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort_characters(left) + middle + quick_sort_characters(right)

def bogo_sort_characters(s):
    arr = list(s)
    while not is_sorted_characters(arr):
        random.shuffle(arr)
    return arr

def is_sorted_characters(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def heap_sort_characters(s):
    arr = list(s)
    heapq.heapify(arr)
    sorted_arr = []
    while arr:
        sorted_arr.append(heapq.heappop(arr))
    return sorted_arr

def radix_sort_characters(s):
    def counting_sort(arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 256

        # Count occurrences of each character
        for char in arr:
            count[ord(char) - ord(' ')] += 1

        # Calculate cumulative count
        for i in range(1, 256):
            count[i] += count[i - 1]

        # Build the output array
        i = n - 1
        while i >= 0:
            output[count[ord(arr[i]) - ord(' ')] - 1] = arr[i]
            count[ord(arr[i]) - ord(' ')] -= 1
            i -= 1

        # Copy the sorted characters back to the original array
        for i in range(n):
            arr[i] = output[i]

    arr = list(s)
    max_digit = len(arr)
    exp = 1
    while max_digit > exp:
        counting_sort(arr, exp)
        exp *= 256

    return arr


'''
cadena = 'pepe pecas'
print("Bubble Sort:", bubble_sort_characters(cadena))
print("Insertion Sort:", insertion_sort_characters(cadena))
print("Selection Sort:", selection_sort_characters(cadena))
print("Merge Sort:", merge_sort_characters(cadena))
print("Quick Sort:", quick_sort_characters(cadena))
print("Bogo Sort:", bogo_sort_characters(cadena))
print("Heap Sort:", heap_sort_characters(cadena))
print("Radix Sort:", radix_sort_characters(cadena))
'''
