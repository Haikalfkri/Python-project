import random 
import string


def generatePassword():
    password_combination = list(string.ascii_letters + string.digits + string.punctuation)
    pwd_length = int(input("How long random password do you want? "))

    random_pwd = []
    for pwd in range(pwd_length):
        random_pwd.append(random.choice(password_combination))
        
    password = "".join(random_pwd)
    print(f"Your password: {password}")
    

if __name__ == "__main__":
    generatePassword()