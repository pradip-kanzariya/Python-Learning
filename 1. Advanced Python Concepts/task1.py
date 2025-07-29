import time

# 1. Advanced Python Concepts

# Practice Task : 1 | Write a decorator to measure the execution time of a function.
def retry(number):
    """
    Decorator which run function given number of times if error occur in function.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            count = 0
            while number > count:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    count += 1
                    print(f"Failed Attemps : {count}")
            print("You have reached maximum amount of faild attemps.")
        return wrapper
    return decorator

def is_admin(user_id):
    """
    Decorator for authentication which identify admin.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            admin_ids = [1,2,3]
            if user_id in admin_ids:
                return func(*args, **kwargs)
            else:
                print("Not Admin.")
        return wrapper
    return decorator

def time_counter(func):
    """
    Decorator which count time in second for given function run.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func_return = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function took : {end_time - start_time} Seconds")
        return func_return
    return wrapper

@is_admin(1)
@retry(3)                               # Chaining multiple decorators.
@time_counter
def login():
    """
    login function.
    """
    user_name = input("Enter Username : ")
    user_password = input("Enter Password : ")

    if user_name == "admin" and user_password == "123":
        print("Login Successfull.")
    else:
        raise ValueError("Invalid Values.")


login()
