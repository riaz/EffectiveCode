from problems.arrays import largest_atleast_twice

def test_largest_atleast_twice():
    assert largest_atleast_twice([3,6,1,0]) == 1
    assert largest_atleast_twice([1,2,3,4]) == -1