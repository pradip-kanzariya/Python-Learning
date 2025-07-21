# 8. Error and Exception Handling

# Practice Task - 1 | Write a division calculator that handles division by zero.
def division_calc():
    """
    Division calculator with error handling.
    """
    try:
        number_1 = float(input("Enter 1st number : "))
        number_2 = float(input("Enter 2nd number : "))
        answer = number_1 / number_2
        print(f"Answer : {answer}")
    except ZeroDivisionError:
        print("Error : Cannot devide by 0.")
    except ValueError:
        print(f"Error : Enter valid value.")
    except TypeError:
        print(f"Error : Enter valid type.")


division_calc()

# Practice Task - 2 | Create a program to validate user input and handle invalid data gracefully.
def validate_user_inputs():
    """
    Validating user inputs like name, age, mobile number with error handling.
    """
    user_name = str(input("Enter name : ").strip())
    if user_name.isalpha():                             # Cheking name is only alphabetic.
        print(f"Valid name : {user_name}")
    else:
        print("Not valid name.")

    try:
        user_age = int(input("Enter age : "))
        print(f"Valid age : {user_age}")
        if user_age <= 0 or user_age > 130:            # Checking age is between 0 to 130.
            print("Not valid age.")
    except ValueError:                                 # Error if input is not integer value.
        print("Invalid value.")

    try:
        user_mobile = input("Enter mobile number : ")
        if len(user_mobile) == 10 and user_mobile.isnumeric():  # Checking if value is numeric and lenth is 10.
            print(f"Valid mobile number : {user_mobile}")
        else:
            print("Invalid mobile number")
    except ValueError:
        print("Invalid values.")


validate_user_inputs()