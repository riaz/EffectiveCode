from algo.unionfind.quickunion import QuickUnion

def test_quickunion():
    uf = QuickUnion(10)

    assert len(uf.arr) == 10 # note: the array was set by the ABC

    assert uf.arr == list(range(len(uf.arr))) # this is what the constructor would assign