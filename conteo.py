import random
import heapq

def bubble_sort(arr):
    n = len(arr)
    c = 0
    for i in range(n):
        c += 1
        for j in range(0, n - i - 1):
            c += 1
            if arr[j] > arr[j + 1]:
                c += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                c += 2
    return c

def insertion_sort(arr):
    c = 0
    for i in range(1, len(arr)):
        c += 1
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            c += 1
            arr[j + 1] = arr[j]
            c += 1
            j -= 1
        arr[j + 1] = key
        c += 1
    return c

def selection_sort(arr):
    c = 0
    for i in range(len(arr)):
        c += 1
        min_idx = i
        for j in range(i + 1, len(arr)):
            c += 1
            if arr[j] < arr[min_idx]:
                c += 1
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        c += 2
    return c

def merge_sort(arr):
    def merge(arr, L, R):
        i = j = k = 0
        c = 0
        while i < len(L) and j < len(R):
            c += 1
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            c += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            c += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            c += 1
        return c
    
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        c = merge_sort(L)
        c += merge_sort(R)
        c += merge(arr, L, R)
        return c
    else:
        return 0

def quick_sort(arr):
    def quick_sort_recursive(arr):
        if len(arr) <= 1:
            return arr, 0
        else:
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            sorted_left, left_count = quick_sort_recursive(left)
            sorted_right, right_count = quick_sort_recursive(right)
            return sorted_left + middle + sorted_right, left_count + right_count + len(arr)
    
    sorted_arr, count = quick_sort_recursive(arr)
    return count

def bogo_sort(arr):
    def is_sorted(arr):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True

    c = 0
    while not is_sorted(arr):
        random.shuffle(arr)
        c += 1
    return c

def heap_sort(arr):
    c = 0
    heapq.heapify(arr)
    sorted_arr = []
    while arr:
        sorted_arr.append(heapq.heappop(arr))
        c += 1
    return c

def radix_sort(arr):
    c=0
    RADIX = 10
    max_digit = len(str(max(arr)))
    for digit in range(max_digit):
        c+=1
        buckets = [[] for _ in range(RADIX)]
        for num in arr:
            c+=1
    return c
