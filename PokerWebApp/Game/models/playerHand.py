from django.db import models

class PlayerHand(models.Model):

    first_card = models.CharField(max_length=4, default = "")
    second_card = models.CharField(max_length=4, default = "")

    # Public methods
    def get_hand_string(self):
        return str(self.first_card) + ',' + str(self.second_card)

    def get_first_card(self):
        return self.first_card

    def get_second_card(self):
        return self.second_card
        
    def deal_card(self, card):
        if (self.first_card == ""):
            self.first_card = card
            return
        elif (self.second_card == ""):
            self.second_card = card
            return
        raise RuntimeError("Dealer is drunk. Giving three cards to a player.")
    
    def take_hand_from_player(self):
        self.first_card = ""
        self.second_card = ""
        