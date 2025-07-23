
def my_multiplication_function(Number_1: int|float, Number_2: int|float) -> int|float|None:
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
        1. my_multiplication_function(5, 5) -> 25 (int)
        2. my_multiplication_function(5, 5.5) -> 27.5 (float)
        3. my_multiplication_function(5, True) -> None
        4. my_multiplication_function("5", 5) -> None
    """
    try:
        return Number_1 * Number_2
    except TypeError:
        print("Error : enter valid type of value.")
        return None