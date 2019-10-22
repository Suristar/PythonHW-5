import analysis

def test_average():
    avg = analysis.average_inflammations(0)
    assert(avg == 5.45)

def test_max():
    avg = analysis.max_inflammations(0)
    assert(avg == 18.0)

def test_acute_patient():
    avg = analysis.average_inflammations(1)
    assert(avg == 5.425) 