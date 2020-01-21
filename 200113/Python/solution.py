def is_shifted(a, b):
    for i in range(len(a)):
        if a[i:] + a[:i] == b:
            return True
    return False

def test_1():
    a = 'abcde'
    b = 'cdeab'
    assert is_shifted(a, b)==True

def test_2():
    a = 'abc'
    b = 'acb'
    assert is_shifted(a, b)==False