"""
Generate a strong password based on user demand.
A strong password is a combination of lowercase,uppercase string,special character and digits

"""

# this module is generated in this app
from main import gen_strong_pass

if __name__ == '__main__':
    print("Password generator app")
    print("*" * 100)

    while True:
        # ask from the user how long password he/she is requiring
        password = input("how long you want password?")
        # validating the user input
        if password.isnumeric():
            print(gen_strong_pass(True, int(password)))
        else:
            print("please write only numbers")
            continue
        # if user demands to generate more password

        if input("Do you want to generator more password:").strip().lower() == "yes":
            continue
        else:
            break
