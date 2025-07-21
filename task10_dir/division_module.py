
def my_division_function(Number_1: int|float, Number_2: int|float) -> float|None:
    """
    Sum of `Number_1` and `Number_2`.

    Parameters :
    ----------
    Number_1 : int | float
    Number_2 : int | float

    Returns :
    -------
        float | None

    Example :
    -------
        1. my_division_function(10, 5) -> 2.0 (float)
        2. my_division_function(5, True) -> None
        3. my_division_function("5", 5) -> None
        4. my_division_function(2, 0) -> None
    """
    if isinstance(Number_1,bool) or isinstance(Number_2, bool):
        return None
    
    try:
        return Number_1 / Number_2
    except TypeError:
        return None
    except ZeroDivisionError:
        return None