from gestures import Gestures
from human import Human
from computer import Computer
import random

class RunGame:
    def __init__(self):
        self.player1 = Human("Player 1")
        self.player2 = Human('Player 2')
        self.computer = Computer()

    def run_game(self):
        self.display_welcome()
        self.display_rules()
        game_mode = self.choose_game_mode()
        if game_mode == True:
            self.player_vs_player()
        else:
            self.player_vs_ai()

    def display_welcome(self):
        print('\n--- Welcome to Rock Paper Sissiors Lizard Spock! ---')

    def display_rules(self):
        print(f'\n--- So these are the rules of the game! ---\n')
        print(f'Rock beats Sissciors, and Rock beats Lizard!')
        print(f'Paper beats Rock, and Paper beats Spock!')
        print(f'Sissiors beats paper, and Sissiors beats Lizard! ')
        print(f'Lizard beats paper, and Lizard beats Spock!')
        print(f'Spock beats Rock, and Spock beats Sissiors!\n\nKeep these in mind when taking your pick for the round!')
        print(f'\n--- This is a best 2 out of 3 game! ---\n')

    def choose_game_mode(self):
        try:
            user_input = input(f'Please select your game mode:\nEnter 1 for Player VS Player.\nEnter 2 for Player VS AI.\nSelection: ')
            if user_input == '1':
                print("\n--- PVP GAME ---")
                return True
            elif user_input == '2':
                print("\n--- PVE GAME ---")
                return False
        except:
            print(f'Please enter one of the valid inputs')
            return self.choose_game_mode()

    def list_choices(self):
        for item1, item2 in zip(self.player1.gesture_number, self.player1.gestures):
            print(f'{item1}: {item2} ')

    def player_vs_player(self):
        while self.player1.wins != 2 and self.player2.wins != 2:
            self.list_choices()
            player1_input = input(f'\n{self.player1.name} - Please enter a number for your gesture you want to select: ')
            index1 = self.what_is_the_index(player1_input)
            gesture_one = Gestures(self.player1.gestures[index1])
            player2_input = input(f'{self.player2.name} - Please enter a number for your gesture you want to select: ')
            index2 = self.what_is_the_index(player2_input)
            gesture_two = Gestures(self.player2.gestures[index2])
            if gesture_one.gesture == gesture_two.gesture:
                print("Draw! Try Again!")
                self.player_vs_player()
            else:
                results = gesture_one.results(gesture_two.gesture)
                if results == "None":
                    print(f'\n{self.player1.name} won this round!\n')
                    self.player1.wins += 1
                else:
                    print(f'\n{self.player2.name} won this round!\n')
                    self.player2.wins += 1                  
        if self.player1.wins > self.player2.wins:
            print(f"{self.player1.name} Wins!\n")
            self.end_game(0)
        else:
            print(f"{self.player2.name} Wins!\n")
            self.end_game(0)

    def player_vs_ai(self):
        while self.player1.wins != 2 and self.computer.wins != 2:
            self.list_choices()
            player1_input = input(f'\n{self.player1.name} - Please enter a number for your gesture you want to select: ')
            index1 = self.what_is_the_index(player1_input)
            gesture_one = Gestures(self.player1.gestures[index1])
            computer_input = str(random.randrange(1, 5))
            index2 = self.what_is_the_index(computer_input)
            gesture_two = Gestures(self.computer.gestures[index2])
            if gesture_one.gesture == gesture_two.gesture:
                print("Draw! Try Again!")
                self.player_vs_ai()
            else:
                results = gesture_one.results(gesture_two.gesture)
                if results == "None":
                    print(f'\n{self.player1.name} won this round!\n')
                    self.player1.wins += 1
                else:
                    print(f'\n{self.computer.name} won this round!\n')
                    self.computer.wins += 1
        if self.player1.wins > self.computer.wins:
            print(f"{self.player1.name} Wins!\n")
            self.end_game(0)
        else:
            print(f"{self.computer.name} Wins!\n")
            self.end_game(0) 

    def what_is_the_index(self, playerinput):
        if playerinput == '1':
            return int(0)
        elif playerinput == '2':
            return int(1)
        elif playerinput == '3':
            return int(2)
        elif playerinput == '4':
            return int(3)
        elif playerinput == '5':
            return int(4)

    def end_game(self, reset_code):
        loop = True
        if reset_code == 0:
            self.player1.wins = 0
            self.player2.wins = 0
            self.computer.wins = 0
        while loop is True:
            user_input = input("Would you like to play again(y/n)? ")
            if user_input == 'y':
                self.run_game()
            elif user_input == 'n':
                print("Thank you for playing.")
                loop = False
            else:
                print("please use the 'y' and 'n' keys to make a selection."