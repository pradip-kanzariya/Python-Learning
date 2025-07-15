# 4. Functions

# Practice Task - 1 | Create a function to find the factorial of a number.
# Using Recursion, Withou loop.
def number_of_factorial(number: int) -> int:
    """ 
    Returns `number` of factorial.

    Parameters
    ----------
    number : int

    Returns
    -------
    int or None

        example: number_of_factorial(5) -> 5 x 4 x 3 x 2 x 1 = 120 or number_of_factorial(True) -> None
    """
    if not isinstance(number, int) or isinstance(number, bool) or number < 0:
        return None
    
    if number == 0 or number == 1:
        return 1
    
    return number * number_of_factorial(number-1)
    

print(number_of_factorial(5))


# Using for loop.
def num_of_factorial(num: int) -> int:
    """ 
    Returns `num` of factorial.

    Parameters
    ----------
    num : int

    Returns
    -------
    int or None

        example: num_of_factorial(5) -> 5 x 4 x 3 x 2 x 1 = 120 or num_of_factorial(True) -> None
    """
    if not isinstance(num, int) or isinstance(num, bool) or num < 0:
        return None
    
    a = 1
    b = 1
    for x in range(1, num+1):
        a = b * x
        b = a
    return b


print(num_of_factorial(5))



# Practice Task - 2 | Create a recursive function for the Fibonacci series.