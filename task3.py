# 3. Control Flow

# Practice Task - 1 | Write a program to check if a number is even or odd.
def odd_or_even(number: int) -> str:
    """
    Return whether the given number is odd or even.

    Parameters
    ----------
    number : int

    Returns
    -------
    str
        Example: if number = 2 -> '2 is even number' else 'Wrong input: True'
    """
    if isinstance(number, int) and not isinstance(number, bool):        # check number is integer and also not boolean. 
        if number % 2 == 0:                                             # check remainder of number is 0 after  division by 2.
            return f"{number} is even number."
        else:
            return f"{number} is odd number."
    else:
        return f"Wrong input: {number}"


print(odd_or_even(5))


# Practice Task - 2 | Print the first 10 numbers of a Fibonacci sequence.
def fibonacci_sequence(number: int) -> list:
    """
    Return a list containing the Fibonacci sequence up to `number` terms.

    Parameters
    ----------
    number : int

    Returns
    -------
    list
        example: If number = 2 → returns [0, 1]
    """

    if not isinstance(number, int) or isinstance(number, bool) or number <= 0:      # check number is integer and positive
        return []
    
    fibonacci_list = [0]
    a = 0
    b = 1
    for x in range(number):
        if len(fibonacci_list) < number:                # check length of list is lower then number 
            c = a + b
            fibonacci_list.append(c)
            a = fibonacci_list[-1]
            b = fibonacci_list[-2]
        else:
            break

    return fibonacci_list
    

print(fibonacci_sequence(10))
