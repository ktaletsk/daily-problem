import pytest

def abspath(path):
    # Check if using Windows or Unix path
    if ('/' in path) == ('\\' in path):
        raise ValueError 
    else:
        separator = '/' if '/' in path else '\\'

        split = path.split(separator)
        result = []
        for p in split:
            if p == '..':
                result.pop(-1)
            elif p != '.':
                result.append(p)
        return separator.join(result)

def test_unix_path():
    assert abspath('/Users/Joma/Documents/../Desktop/./../') == '/Users/Joma/'

def test_windows_path():
    assert abspath('C:\\Windows') == 'C:\\Windows'

def test_bad_path():
    with pytest.raises(Exception) as e_info:
        abspath('C:\\Windows/')