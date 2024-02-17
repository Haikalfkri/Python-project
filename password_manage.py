def add():
    name = input("Account Name: ")
    password = input("Enter Password: ")
    
    with open("passwords.txt", "a") as f:
        f.write(name + " | " + password + "\n")

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            name, pwd = data.split("|")
            print("Name: " + name + "| " + "Password: " + pwd)

def main():
    while True:
        mode = input("Enter the mode add password or view existing password (add, view) or q to quit: ").lower()

        if mode == "q":
            break;

        if mode == "add":
            add()
        elif mode == "view":
            view()
        else:
            print("You enter invalid mode.")
            

if __name__ == "__main__":
    main()