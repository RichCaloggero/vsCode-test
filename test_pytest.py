from t import average_rainfall as r

def test_normal ():
    assert r([1,2]) == 1.5

def test_stop ():
    assert r([1,2,-999,77]) == 1.5

def test_invalid():
    assert r([1,-0.2,-6.5,2]) == 1.5


