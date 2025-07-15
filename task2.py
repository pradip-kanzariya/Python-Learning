# 2. Python Syntax and Basics

# Practice Task - 1 | Store and print variables of each type.
integer_variable = 10
float_variable = 10.10
string_variable = "string"
boolean_variable = True
list_variable = [1, 2, 3, 4]
tuple_variable = (1, 2, 3, 4)
set_variable = {1, 2, 3, 4}
dictionary_variable = {"one": 1, "two": 2, "three":3}
none_type_var = None

print(f"Integer : {integer_variable}")
print(f"Float : {float_variable}")
print(f"String : {string_variable}")
print(f"Boolean : {boolean_variable}")
print(f"List : {list_variable}")
print(f"Tuple : {tuple_variable}")
print(f"Set : {set_variable}")
print(f"Dictionary : {dictionary_variable}")
print(f"None : {none_type_var}")


# Practice Task - 2 | Concatenate and format strings using f-strings.
def display_fullname(first_name, last_name):
    """ Display fullname. """
    full_name = first_name + " " + last_name        # string concatenate
    print(f"Your fullname is {full_name}")          # f-string use


display_fullname("Pradip", "Kanzariya")