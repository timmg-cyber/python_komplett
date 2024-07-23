import doctest

def is_even(number):
## 1 create docstring with shell output
    """
    >>> is_even(2)
    True
    >>> is_even(7)
    False

    """
    if number%2 == 0:
        return True
    else:
        return False


def contains_sequence(text, sequence):
    """
    >>> contains_sequence("Mein Name ist Timm","Tom")
    False
    >>> contains_sequence("Mein Name ist Timm", "Timm")
    True

    """
    if sequence in text:
        return True
    else:
        return False


## 2 Create main-method
if __name__ == "__main__":
    doctest.testmod()
