import random


class paperRockScissor:
    def __init__(self, name):
        self.name = name

    def user_input(self):
        userInput = input(
            f"{self.name} enter your choice (rock, paper, scissor): ").lower()

        return userInput

    def computer_choice(self):
        choice = ["Rock", "Paper", "Scissor"]
        computer_choice = random.choice(choice).lower()

        return computer_choice

    def play_game(self):
        print("Welcome to rock paper scissor game")
        continueInput = input(
            "Do you want to continue the game (yes/no): ").lower()

        while continueInput == "yes":
            user_choice = self.user_input()
            print("Computer pick", self.computer_choice())

            if self.computer_choice() == user_choice:
                print("You tie")
            elif (
                (self.computer_choice() == "rock" and user_choice == "scissor") or
                (self.computer_choice() == "scissor" and user_choice == "paper") or
                (self.computer_choice() == "paper" and user_choice == "rock")
            ):
                print("you lose")
            else:
                print("you win")
                
            continueInput = input(
            "Do you want to continue the game (yes/no): ").lower()
        
        print("Game over, thanks for playing")


if __name__ == "__main__":
    player_name = input("Player name: ")
    game = paperRockScissor(player_name)
    game.play_game()