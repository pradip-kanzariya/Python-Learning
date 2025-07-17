# 6. Basic Modules

import random
import os

# Practice Task - 1 | Generate a random number between 1 and 100.
def random_number_generator():
    """ Generate random number between 1 to 100 using random module."""
    random_number = random.randint(1, 100)              # Using '.randint()' function to get random integer number between 1 to 100.
    return random_number


print(f"Task-1 : {random_number_generator()}")


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
