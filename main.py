import random
import string


def gen_strong_pass(pass_want):
    strg_pass = ""
    if pass_want:
        i = 0
        while i < 10:
            if 0 > i < 3:
                strg_pass += random.choice(string.ascii_lowercase)
            elif 3 > i < 5:
                strg_pass += random.choice(string.ascii_uppercase)

            elif 5 > i < 8:
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
    print("The Generated Password :", gen_strong_pass(True))
    while 1:

        if input("Do you want to create more password:").strip().lower() == "yes":
            print("The Generated Password :", gen_strong_pass(True))
        else:
            gen_strong_pass(False)
