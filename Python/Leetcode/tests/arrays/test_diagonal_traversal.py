from problems.arrays.diagonal_traversal import Solution

def test_diagonal_traversal():
    s = Solution()
    
    arr = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    expected = [1,2,4,7,5,3,6,8,9]
    got = s.findDiagonalOrder(arr)

    assert got == expected

    arr = [[1,2],[3,4]]
    assert s.findDiagonalOrder(arr) == [1,2,3,4]