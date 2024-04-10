def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Example usage:
numbers = [5, 2, 4, 6, 1, 3]
print("Original List:", numbers)
print("Sorted List:", selection_sort(numbers))
