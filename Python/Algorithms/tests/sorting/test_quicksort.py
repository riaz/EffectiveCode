from algo.sorting import quicksort

def test_quicksort():
    arr = [5,6,2,5,1,4]
    arr_expect = [1,2,4,5,5,6]
    assert quicksort.sort(arr) == arr_expect