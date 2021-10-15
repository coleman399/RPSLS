class Gestures:
    def __init_(self, gesture):
        self.gesture = gesture
        self.defeats = {}
        if self.gesture == "rock":
            self.defeats.update({"scissors": "beats"})
            self.defeats.update({"lizard": "beats"})
        elif self.gesture == "paper":
            self.defeats.update({"rock": "beats"})
            self.defeats.update({"spock": "beats"})
        elif self.gesture == "scissors":
            self.defeats.update({"paper": "beats"})
            self.defeats.update({"lizard", "beats"})
        elif self.gesture == "lizard":
            self.defeats.update({"paper": "beats"})
            self.defeats.update({"spock": "beats"})
        elif self.gesture == "spock":
            self.defeats.update({"scissors": "beats"})
            self.defeats.update({"rock": "beats"})

    def result(self, player_one_choice, player_two_choice):
        if player_two_choice in self.defeats.keys():
            return self.defeats[player_two_choice]
        else:
            return "None"
