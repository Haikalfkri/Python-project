import random


def number_guessing_game():
    heart = 0
    end = False
    
    random_number = random.randint(1, 20)
    
    mode = input("Easy or Hard Mode? ").lower()
    
    if mode == "easy":
        heart = 10
        print(f"Your have {heart} chance")
        print("Guess number between 1-20")
        
        while not end:
            user_guess = int(input("Enter your answer: "))
            
            if user_guess == random_number:
                print("You Right!!")
                end = True
            else:
                if heart != 0:
                    print("You Wrong!")
                    print(f"You heart {heart}")
                    heart -= 1            
                elif heart == 0:
                    print("You lose your heart, you lose!!")
                    end = True
    elif mode == "hard":
        heart = 5
        print(f"Your have {heart} chance")
        print("Guess number between 1-20")
        
        while not end:
            user_guess = int(input("Enter your answer: "))
            
            if user_guess == random_number:
                print("You Right!!")
                end = True
            else:
                if heart != 0:
                    print("You Wrong!")
                    print(f"You heart {heart}")
                    heart -= 1            
                elif heart == 0:
                    print("You lose your heart, you lose!!")
                    end = True
    else:
        print("You enter wrong command, please try again!!")
        
        
number_guessing_game()