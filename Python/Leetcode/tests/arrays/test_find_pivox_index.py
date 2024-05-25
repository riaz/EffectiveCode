from problems.arrays import find_pivox_index

def test_find_pivox_index():
    assert find_pivox_index([1]) == 0
    assert find_pivox_index([1,7,3,6,5,6]) == 3
    assert find_pivox_index([1,2,3]) == -1
    assert find_pivox_index([2,1,-1]) == 0