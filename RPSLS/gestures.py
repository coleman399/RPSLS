class Gestures:
    def __init__(self, input):
        self.gesture = input
        self.defeats = {}
        if self.gesture == 'rock':
            self.defeats.update({'scissors': "beats"})
            self.defeats.update({'lizard': "beats"})
        elif self.gesture == 'paper':
            self.defeats.update({'rock': "beats"})
            self.defeats.update({'spock': "beats"})
        elif self.gesture == 'scissors':
            self.defeats.update({'paper': "beats"})
            self.defeats.update({'lizard': "beats"})
        elif self.gesture == 'lizard':
            self.defeats.update({'paper': "beats"})
            self.defeats.update({'spock': "beats"})
        elif self.gesture == 'spock':
            self.defeats.update({'scissors': "beats"})
            self.defeats.update({'rock': "beats"})

    def results(self, player_two_choice):
        if player_two_choice in self.defeats:
            return 
        else:
            return "None"
