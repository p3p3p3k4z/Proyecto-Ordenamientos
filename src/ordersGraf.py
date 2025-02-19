import random
import heapq

def bubble_sort(arr):
    n = len(arr)
    frames = [arr.copy()]
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                frames.append(arr.copy())
    return frames

def insertion_sort(arr):
    frames = [arr.copy()]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        frames.append(arr.copy())
    return frames

def selection_sort(arr):
    frames = [arr.copy()]
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        frames.append(arr.copy())
    return frames

def merge_sort(arr):
    frames = []

    def merge_sort_helper(arr, left, right):
        if left < right:
            mid = (left + right) // 2
            merge_sort_helper(arr, left, mid)
            merge_sort_helper(arr, mid + 1, right)
            merge(arr, left, mid, right)
            frames.append(arr.copy())

    def merge(arr, left, mid, right):
        L = arr[left:mid + 1]
        R = arr[mid + 1:right + 1]
        i = j = 0
        k = left
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    merge_sort_helper(arr, 0, len(arr) - 1)
    return frames

def quick_sort(arr):
    frames = []
    
    def quick_sort_helper(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            frames.append(arr.copy())
            quick_sort_helper(arr, low, pi-1)
            quick_sort_helper(arr, pi+1, high)

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    quick_sort_helper(arr, 0, len(arr) - 1)
    return frames

def bogo_sort(arr):
    frames = [arr.copy()]
    while not is_sorted(arr):
        random.shuffle(arr)
        frames.append(arr.copy())
    return frames

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def heap_sort(arr):
    frames = [arr.copy()]
    heapq.heapify(arr)
    frames.append(arr.copy())
    sorted_arr = []
    while arr:
        sorted_arr.append(heapq.heappop(arr))
        frames.append(sorted_arr + arr)
    return frames

def radix_sort(arr):
    RADIX = 10
    frames = [arr.copy()]
    max_digit = len(str(max(arr)))
    for digit in range(max_digit):
        buckets = [[] for _ in range(RADIX)]
        for num in arr:
            buckets[(num // RADIX ** digit) % RADIX].append(num)
        arr = [num for bucket in buckets for num in bucket]
        frames.append(arr.copy())
    return frames
