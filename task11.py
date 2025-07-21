from collections import Counter

# 11. Advanced Data Structures

# Practice Task : 1 | Create a frequency counter for characters in a string.
def frequency_counter():
    """
    Frequency counter for characters in a string.
    """
    my_string = input("Enter string : ")
    return Counter(my_string)


print(frequency_counter())


# Practice Task : 2 | Implement a queue using deque.
