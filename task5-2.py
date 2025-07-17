# 5. Data Structures

# Practice Task - 2 | Implement a program to find duplicates in a list using sets.
def find_duplicates(list_with_duplicates):
    """
    Find duplicate values from list containing duplicate values using sets.

    Paramaters
    ----------
    list_with_duplicates : list

    Returns
    -------
        list

    Example : find_duplicates(list_with_duplicates) -> [1, 2, 3, 5]
    """
    set_variable = set()
    set_variable_duplicate = set()
    for each in list_with_duplicates:
        
        if each in set_variable:
            set_variable_duplicate.add(each)
        else:
            set_variable.add(each)

    return list(set_variable_duplicate)


list_with_duplicates = [1, 0, 2, 50, 1, 5, 10, 2, 5, 9, 11, 50, 3, 3, 50]
print(find_duplicates(list_with_duplicates))
    