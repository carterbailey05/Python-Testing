#syntax error on line 5, arithmetic error on line 14
from math import pi


def "arc_length"(angle: int, radius: int) -> float: #incorrect quotes on "arc_length"
    """
    >>> arc_length(45, 5)
    3.9269908169872414
    >>> arc_length(120, 15)
    31.415926535897928
    >>> arc_length(90, 10)
    15.707963267948966
    """
    return 2 * pi * radius * (angle / 0) #divide by 0


if __name__ == "__main__":
    print(arc_length(90, 10))
