class Gestures:
    def __init__(self, input):
        self.gesture = input
        self.defeats = []
        if self.gesture == 'rock':
            self.defeats.append('scissors')
            self.defeats.append('lizard')
        elif self.gesture == 'paper':
            self.defeats.append('rock')
            self.defeats.append('spock')
        elif self.gesture == 'scissors':
            self.defeats.append('paper')
            self.defeats.append('lizard')
        elif self.gesture == 'lizard':
            self.defeats.append('paper')
            self.defeats.append('spock')
        elif self.gesture == 'spock':
            self.defeats.append('scissors')
            self.defeats.append('rock')

    def results(self, player_two_choice):
        if player_two_choice in self.defeats:
            return 
        else:
            return 0
