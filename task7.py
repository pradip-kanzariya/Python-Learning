# 7. File Handling
import json

# Practice Task - 1 | Write a program to count the number of lines in a file.
with open("new_file.txt", "r") as f:
    f_read = f.readlines()

    print(f"Task 1 : {len(f_read)}")


# Practice Task - 2 | Create a JSON file to store user data and write a program to update it.
def user_data():
    """
    Create json file with user information and update information.
    """
    print("1. : Create user.")
    print("2. : Update user.")
    user_input = input("Choose option '1' or '2' : ").strip()

    if user_input == "1":
        persons_data_list = []
        user_name = input("Enter Name : ").strip()
        user_age = input("Enter Age : ").strip()
        user_hobbies = [hobby.strip() for hobby in input("Enter Hobbies : ").split(",")]
        if "" in user_hobbies:
            user_hobbies = None
        person_data = {"Name": user_name, "Age": user_age, "Hobbies": user_hobbies}

        try:
            with open("users_file.json", "r") as file:
                old_data = json.load(file)
                if old_data:
                    persons_data_list.extend(old_data)
                persons_data_list.append(person_data)
        except Exception as e:
            print(f"Error : {e}")
            persons_data_list.append(person_data)

        with open("users_file.json", "w") as file:
            json.dump(persons_data_list, file, indent=4)                                                                                                                                 
            print("User Created in json file.")

    elif user_input == "2":
        try:
            with open("users_file.json", "r") as file:
                file_data = file.read()
                file_data = json.loads(file_data)
                user_input_name = input("Enter existing 'Name' you want to update. : ").strip()
                switch = False
                for data in file_data:
                    if data["Name"] == user_input_name:
                        print(f"Found : {data}")
                        input_user_name = input("Enter new 'Name' : ").strip()
                        input_user_age = input("Enter new 'Age' : ").strip()
                        input_user_hobbies = [hobby.strip() for hobby in input("Enter new 'Hobbies' : ").split(",")]
                        if "" in input_user_hobbies:
                            input_user_hobbies = None
                        data["Name"] = input_user_name
                        data["Age"] = input_user_age
                        data["Hobbies"] = input_user_hobbies
                        switch = True
                        break
                if switch == False:
                    print("User not found.")
                    return
            with open("users_file.json", "w") as file:
                file_data_json = json.dumps(file_data)
                file.write(file_data_json)
                print("User Updated.")
        except Exception as e:
            print(f"Erorr : {e}")

    else:
        print("Invalid input.")

user_data()