from algo.unionfind.quickunion import QuickUnion

def test_quickunion():
    N = 10
    uf = QuickUnion(N)

    assert len(uf.arr) == 10 # note: the array was set by the ABC

    assert uf.arr == list(range(len(uf.arr))) # this is what the constructor would assign

    uf.union(0,1)
    uf.union(5,9)
    uf.union(3,4)

    assert uf.connected(0,1) == True
    
    assert uf.connected(0,5) == False

    assert uf.connected(7,8) == False

    assert uf.num_of_components() == 7

    uf.union(0,2)
    uf.union(7,8)

    assert uf.connected(0,2) == True

    assert uf.num_of_components() == 5

    uf.union(0, 4)

    assert uf.connected(2, 3) == True

    assert uf.num_of_components() == 4

    uf.union(3, 6)
    uf.union(8, 6)

    assert uf.num_of_components() == 2

    assert uf.connected(1,7) == True

    uf.union(7, 9)

    assert uf.num_of_components() == 1

    # At this point everything is connected

    assert uf.connected(1,1) # reflection

    assert uf.connected(3, 4) == uf.connected(4, 3) # symmetry

    assert uf.connected(1,2) == uf.connected(2, 5) == uf.connected(5, 7) == uf.connected(1,7) # equivalence