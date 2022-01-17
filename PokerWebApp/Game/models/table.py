from locale import currency
from django.db import models
from Game.models import PlayerHand, Deck

class Table(models.Model):

    currentPlayers = []
    isGameRunning = models.BooleanField(default = False)

    # private

    def __init__(self):
        self.__numberOfPlayers = 8
        self.__deck = Deck()
        self.isGameRunning = False
        for _ in range(self.__numberOfPlayers):
            playerHand = PlayerHand()
            self.currentPlayers.append(playerHand)
        

    def start_game(self):
        self.__take_hand_from_players()
        self.__deck.shuffle_deck()
        self.isGameRunning = True
        for playerHand in self.currentPlayers:
            playerHand.deal_card(self.__deck.deal_card())
        for playerHand in self.currentPlayers:
            playerHand.deal_card(self.__deck.deal_card())

    def get_context(self):
        jsonData = {}
        for index, playerHand in enumerate(self.currentPlayers):
            playerID = "p" + str(index + 1)
            hand = playerHand.get_hand_string()
            jsonData[playerID] = hand
        return jsonData

    def __take_hand_from_players(self):
        for playerHand in self.currentPlayers:
            playerHand.take_hand_from_player()