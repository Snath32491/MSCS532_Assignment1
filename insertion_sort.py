# insertion_sort.py

def insertion_sort_descending(arr):
    """Sorts an array in monotonically decreasing order using the Insertion Sort algorithm."""
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are less than key, to one position ahead of their current position
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

# Example usage:
if __name__ == "__main__":
    data = [5, 2, 9, 1, 5, 6]
    print("Original array:", data)
    sorted_data = insertion_sort_descending(data)
    print("Sorted array (monotonically decreasing):", sorted_data)
