# 1. Advanced Python Concepts

# Practice Task : 4 | Use dictionary comprehension to invert a dictionary (keys become values and vice versa).
def tans_dict():
    """Convert key to value and value to key for dictionary."""
    dict_a = {
        1: "One",
        2: "Two",
        3: "Three"
    }
    output_dict = {value:key for key,value in dict_a.items()}
    return output_dict

print(tans_dict())