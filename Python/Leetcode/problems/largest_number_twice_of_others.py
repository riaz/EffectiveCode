def largest_atleast_twice(arr: list[int]) -> int:
    """
    pick the largest in the array
    if the largest is atleast 2x greater or equal to rest return index of largest 
    else return -1
    """

    n = len(arr)
    index_max = max(range(n), key=arr.__getitem__)
    for i in range(n):
        if i != index_max and (2 * arr[i] ) > arr[index_max]:
                return -1
    return index_max
