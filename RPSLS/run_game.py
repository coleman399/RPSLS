from gestures import Gestures
from human import Human
from computer import Computer
import random



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
        print(f'Welcome {self.player1_name} and {self.player2_name} \nto Rock Paper Sissiors Lizard Spock! ')

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
            player1_input = input(f'{self.player1_name.name} Please enter a number for your gesture you want to select')
            gesture_one = Gestures(player1_input)
            player2_input = input(f'{self.player2_name.name} Please enter a number for your gesture you want to select')
            gesture_two = Gestures(player2_input)

            result = gesture_one.result(gesture_one, gesture_two)

            if result != "None":
                self.player1_name.wins += 1
            else:
                self.player2_name.wins += 1


    def player_vs_ai(self):
        pass

    