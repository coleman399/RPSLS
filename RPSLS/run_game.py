from gestures import Gestures
from human import Human
from computer import Computer
import random
import sys



class RunGame:
    def __init__(self):
        self.player1_name = Human("Wes")
        self.player2_name = Human('Dillon')


    def run_game(self):
        self.display_welcome()
        self.display_rules()
        game_mode = self.choose_game_mode()
        if game_mode == True:
            self.player_vs_player()
        else:
            self.player_vs_ai()


    def display_welcome(self):
        print(f'Welcome {self.player1_name.name} and {self.player2_name.name} \nto Rock Paper Sissiors Lizard Spock! ')

    def display_rules(self):
        print(f'\nSo these are the rules of the game!')
        print(f'\n Rock beats Sissciors, and Rock beats Lizard!')
        print(f'Paper beats Rock, and Paper beats Spock')
        print(f'Sissiors beats paper, and Sissiors beats Lizard! ')
        print(f'Lizard beats paper, and Lizard beats Spock')
        print(f'Spock beats Rock, and Spock beats Sissiors! \nKeep these in mind when taking your pick for the round!')
        print(f'\n This is a best 2 out of 3 game! ')

    def choose_game_mode(self):
        try:
            user_input = input(f'Please select your game mode: Enter 1 for Player VS Player; Enter 2 for Player VS AI: ')
            if user_input == '1':
                return True
            elif user_input == '2':
                return False
        except:
            print(f'Please enter one of the valid inputs')
            return self.choose_game_mode()

    def list_choices(self):
        for item1, item2 in zip(self.player1_name.gesture_number, self.player1_name.gestures):
            print(f'{item1}: {item2} ')

    def player_vs_player(self):
        while self.player1_name.wins != 2 and self.player2_name.wins != 2:
            self.list_choices()
            player1_input = input(f'{self.player1_name.name} Please enter a number for your gesture you want to select: ')
            index1 = self.what_is_the_index(player1_input)
            gesture_one = Gestures(self.player1_name.gestures[index1])
            player2_input = input(f'{self.player2_name.name} Please enter a number for your gesture you want to select: ')
            index2 = self.what_is_the_index(player2_input)
            gesture_two = Gestures(self.player2_name.gestures[index2])
            if gesture_one.gesture is gesture_two.gesture:
                print("Draw! Try Again!")
                self.player_vs_player()
            else:
                results = gesture_one.results(gesture_two.gesture)
                if results == "None":
                    print(f'{self.player1_name.name} won this round!')
                    self.player1_name.wins += 1
                else:
                    print(f'{self.player2_name.name} won this round!')
                    self.player2_name.wins += 1
                        
        if self.player1_name.wins > self.player2_name.wins:
            print(f"{self.player1_name.name} Wins!")
            sys.exit()
        else:
            print(f"{self.player2_name.name} Wins!")
            sys.exit()

    def player_vs_ai(self):
        pass

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
