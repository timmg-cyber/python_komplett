import pytest

from my_module import is_even, contains_sequence

#auto detection of tests shows a play button
#assert ist ein debugging statement --> wenn Assertion fails wird Programm unterbrochen
def test_is_even():
    assert is_even(4) == True
    assert is_even(7) == True

def test_contains_sequence():
    assert contains_sequence("Mein Name ist Timm", "Timm") == True
    assert contains_sequence("Mein Name ist Timm", "Tom") == True

## Test wir gepassed weil man einen TypeError bekommt
def test_is_even_type():
    with pytest.raises(TypeError):
        is_even("Four")
