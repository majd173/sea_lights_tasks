import json


class Account:
    """
    This class manages sign in and sign up process.
    """

    def __init__(self, username, password):
        self._username = username
        self._password = password

    @staticmethod
    def sign_up(username, password):
        """
        This function manages sign up process.
        :param username:
        :param password:        """
        try:
            with open(r'C:\Users\Admin\Desktop\majd\Python_& _Automation\pycharm_sea_lights\calculator\accounts.json', 'r') as f:
                data = json.load(f)
            users = data.get("users", [])
            if any(user["username"] == username for user in users):
                print(f"Sign up failed, {username} already exists.")
                return
            users.append({"username": username, "password": password})
            data["users"] = users
            with open(r'C:\Users\Admin\Desktop\majd\Python_& _Automation\pycharm_sea_lights\calculator\accounts.json', 'w') as f:
                json.dump(data, f, indent=4)
            print(f"Sign up successful, {username} was created.")
        except json.decoder.JSONDecodeError:
            print("Corrupted accounts.json file. Creating a new one.")
            data = {"users": [{"username": username, "password": password}]}
            with open(r"C:\Users\Admin\Desktop\majd\Python_& _Automation\pycharm_sea_lights\calculator\accounts.json", "w") as f:
                json.dump(data, f, indent=4)
            print(f"Sign up successful, {username} was created.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    @staticmethod
    def sign_in(username, password):
        """
        This function manages sign in process.
        :param username:
        :param password:
        """
        try:
            with open(r'C:\Users\Admin\Desktop\majd\Python_& _Automation\pycharm_sea_lights\calculator\accounts.json', 'r') as f:
                data = json.load(f)
            users = data.get("users", [])
            for user in users:
                if user["username"] == username:
                    if user["password"] == password:
                        print(f"Sign in successful, {username} was logged in.")
                        return
                    print("Sign in failed, wrong password.")
                    return
            print(f"Sign in failed, user {username} not found.")
        except FileNotFoundError:
            print("No accounts found. Please sign up first.")
        except json.decoder.JSONDecodeError:
            print("An error occurred while reading the file")
        except Exception as e:
            print(e)

    @staticmethod
    def list_users():
        """
        This function lists all users.
        :return:
        """
        try:
            with open(r'C:\Users\Admin\Desktop\majd\Python_& _Automation\pycharm_sea_lights\calculator\accounts.json', 'r') as f:
                data = json.load(f)
            users = data.get("users", [])
            return [user["username"] for user in users]
        except FileNotFoundError:
            print("An error occurred while reading the file")
            return []
        except json.decoder.JSONDecodeError:
            print("An error occurred while reading the file")
            return []
        except Exception as e:
            print(e)
            return []

    @staticmethod
    def remove_user(username):
        """
        This function removes a user.
        :param username:
        """
        try:
            with open(r'C:\Users\Admin\Desktop\majd\Python_& _Automation\pycharm_sea_lights\calculator\accounts.json', 'r') as f:
                data = json.load(f)
            users = data.get("users", [])
            for user in users:
                if user["username"] == username:
                    users.remove(user)
                    data["users"] = users
                    with open(r'C:\Users\Admin\Desktop\majd\Python_& _Automation\pycharm_sea_lights\calculator\accounts.json', 'w') as f:
                        json.dump(data, f, indent=4)
                    print(f"User: {username} removed successfully")
                    return
            print("User not found")
        except json.decoder.JSONDecodeError:
            print("An error occurred while reading the file")
        except Exception as e:
            print(e)

Account.sign_up("11", "1")