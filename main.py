"""
Strong password generator

This app will generate strong password using random module.
A strong password is a collection of lowercase,uppercase string,punctutation and digits.
"""

import random
import string


def gen_strong_pass(pass_want, long):
    """
    generate a strong password and return that password
    :param pass_want:bool
    :param long: int
    :return: generate a strong password and return that password in form of string
    """
    strg_pass = ""
    if pass_want:
        i = 0
        while i < long:
            if 0 <= i < 3:
                strg_pass += random.choice(string.ascii_lowercase)

            elif 3 <= i < 5:
                strg_pass += random.choice(string.ascii_uppercase)

            elif 5 <= i < 8:
                strg_pass += random.choice(string.punctuation)
            else:
                strg_pass += random.choice(string.digits)
            i += 1
        pass_ = list(strg_pass)
        random.shuffle(pass_)
        return "".join(pass_)
    else:
        exit()


if __name__ == '__main__':
    print("password generator app")
    print("*" * 100)
    print("The Generated Password :", gen_strong_pass(True, 10))

    # if user ask to generate another strong password
    while 1:
        #
        if input("Do you want to create more password:").strip().lower() == "yes":
            print("The Generated Password :", gen_strong_pass(True, 10))
        else:
            gen_strong_pass(False, 10)
