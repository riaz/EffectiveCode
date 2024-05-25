from problems.factorization import factorization

def test_factorization_sample():
    got = factorization(12)
    expected = [2,2,3]
    assert expected in got