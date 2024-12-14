import json
import os


class Account:
    """
    This class manages sign in and sign up process.
    """

    def __init__(self, username=None, password=None):
        self._username = username
        self._password = password
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self._config = os.path.join(base_dir, r'../accounts.json')

    # @staticmethod
    def sign_up(self, username, password):
        """
        This function manages sign up process.
        :param username:
        :param password:        """
        try:
            with open(self._config, 'r') as f:
                data = json.load(f)
            users = data.get("users", [])
            if any(user["username"] == username for user in users):
                print(f"Sign up failed, {username} already exists.")
                return
            users.append({"username": username, "password": password})
            data["users"] = users
            with open(self._config, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"Sign up successful, {username} was created.")
        except json.decoder.JSONDecodeError:
            print("Corrupted accounts.json file. Creating a new one.")
            data = {"users": [{"username": username, "password": password}]}
            with open(self._config, "w") as f:
                json.dump(data, f, indent=4)
            print(f"Sign up successful, {username} was created.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def sign_in(self, username, password):
        """
        This function manages sign in process.
        :param username:
        :param password:
        """
        try:
            with open(self._config, 'r') as f:
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

    def list_users(self):
        """
        This function lists all users.
        :return:
        """
        try:
            with open(self._config, 'r') as f:
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

    def remove_user(self, username):
        """
        This function removes a user.
        :param username:
        """
        try:
            with open(self._config, 'r') as f:
                data = json.load(f)
            users = data.get("users", [])
            for user in users:
                if user["username"] == username:
                    users.remove(user)
                    data["users"] = users
                    with open(r'C:\Users\Admin\Desktop\majd\tricentis\pycharm_sea_lights\calculator\accounts.json',
                              'w') as f:
                        json.dump(data, f, indent=4)
                    print(f"User: {username} removed successfully")
                    return
            print("User not found")
        except json.decoder.JSONDecodeError:
            print("An error occurred while reading the file")
        except Exception as e:
            print(e)
