from src.calculator_class import Calculator
from src.account_class import Account


def main_calculator():
    """
    This function runs the calculator with it's all functions.
    """
    while True:
        try:
            print("Welcome to the calculator app!")
            option = input("Please choose an option:\n1.Addition\n"
                           "2.Subtraction\n3.Multiplication\n4.Division\n"
                           "5. Sign in\n6. Sign up\n7.Exit\n")
            if option == "1":
                first_number = int(input("Please insert first number: "))
                second_number = int(input("Please insert second number: "))
                result = Calculator.addition_function(first_number, second_number)
                print(f'{result}\n')
            elif option == "2":
                first_number = int(input("Please insert first number: "))
                second_number = int(input("Please insert second number: "))
                result = Calculator.subtraction_function(first_number, second_number)
                print(f'{result}\n')
            elif option == "3":
                first_number = int(input("Please insert first number: "))
                second_number = int(input("Please insert second number: "))
                result = Calculator.multiplication_function(first_number, second_number)
                print(f'{result}\n')
            elif option == "4":
                first_number = int(input("Please insert first number: "))
                second_number = int(input("Please insert second number: "))
                result = Calculator.division_function(first_number, second_number)
                print(f'{result}\n')
            elif option == "5":
                username = input("Please insert username: ")
                password = input("Please insert password: ")
                user = Account()
                user.sign_in(username, password)
                continue
            elif option == "6":
                username = input("Please insert username: ")
                password = input("Please insert password: ")
                user = Account()
                user.sign_up(username, password)
                continue
            elif option == "7":
                print("Goodbye!")
                exit()
            else:
                print("Please insert a correct option.")
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main_calculator()
