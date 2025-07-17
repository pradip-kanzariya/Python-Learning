# 6. Basic Modules

import random
import os

# Practice Task - 1 | Generate a random number between 1 and 100.
def random_number_generator():
    """ Generate random number between 1 to 100 using random module."""
    random_number = random.randint(1, 100)              # Using '.randint()' function to get random integer number between 1 to 100.
    return random_number


print(f"Task-1 : {random_number_generator()}")


# Practice Task - 1.1 | Generate a random number between 1 and 100 without using random module and with pure core python logic.
def generate_random_number():
    """
    Generate a random number between 1 and 100 without any module and using core python.
    """
    num_list = []
    second_list = []
    number = 1.1
    number_id = id(number)
    str_number_id = str(number_id)
    num_list.extend(str_number_id)

    if num_list[-3] == "1" and num_list[-2] == "0" and num_list[-1] == "0":
        second_list.append(num_list[-3])
        second_list.append(num_list[-2])
        second_list.append(num_list[-1])
    else:
        if num_list[-2] == "0":
            second_list.append(num_list[-1])
        else:
            second_list.append(num_list[-2])
            second_list.append(num_list[-1])

    str_join = "".join(second_list)
    int_num = int(str_join)

    return int_num


print(f"Task-1.1 : {generate_random_number()}")


# Practice Task - 2 | Create a program that lists all files in a directory.
def dir_list_files(directory_path: str) -> list:
    """
    Get list of all files names by passing `directory_path`.

    Parameters
    ----------
    directory_path : `str`

    Returns
    ------
        return datatype : `list`

    Example
    -------
        `dir_list_files(directory_path=os.getcwd())` `->` `['.git', 'README.md', 'task1.py']`
    """
    dir_list = os.listdir(directory_path)                       # Lists all filenames using '.listdir()' function.
    return dir_list


print(f"Task-2 : {dir_list_files(directory_path=os.getcwd())}") # To get current working directory path or path of the directory.
