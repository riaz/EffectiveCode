from problems.arrays.plus_one import Solution

def test_plus_one():
    s = Solution()
    assert s.plusOne([1,2,3]) == [1,2,4]
    assert s.plusOne([4,3,2,1]) == [4,3,2,2]
    assert s.plusOne([9]) == [1,0]