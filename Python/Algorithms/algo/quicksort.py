def sort(arr: list[int]) -> list[int]:
    if len(arr) < 1:
        return arr
    pivot = arr[len(arr) // 2]
    
    left = [x for x in arr if x < pivot] # less than pivot
    middle = [x for x in arr if x == pivot] # equal to pivot
    right = [x for x in arr if x > pivot] # greater than pivot

    return sort(left) + middle + sort(right)

