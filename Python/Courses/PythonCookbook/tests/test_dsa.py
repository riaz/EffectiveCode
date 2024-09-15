from cookbook.dsa import DSA

def test_get_historical_data():
    lst = [
        "apple1",
        "apple2",
        "apple3",
        "apple4",
        "apple5",
        "apple6",
        "apple7",
    ]

    hist = 3
    dsa = DSA()
    idx = 0
    for line, history in dsa.get_historial_data(lst, hist):
        print(history)
        assert line == lst[idx]
        idx +=1