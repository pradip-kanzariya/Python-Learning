
def my_addition_function(Number_1: int|float, Number_2: int|float) -> int|float|None:
    """
    Sum of `Number_1` and `Number_2`.

    Parameters :
    ----------
    Number_1 : int | float
    Number_2 : int | float

    Returns :
    -------
        int | float | None

    Example :
    -------
        1. my_sum_function(5, 5) -> 10 (int)
        2. my_sum_function(5, 5.5) -> 10.5 (float)
        3. my_sum_function(5, True) -> None
        4. my_sum_function("5", 5) -> None
    """
    if isinstance(Number_1,bool) or isinstance(Number_2, bool):
        return None
    
    try:
        return Number_1 + Number_2
    except TypeError:
        return None