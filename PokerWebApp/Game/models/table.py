from locale import currency
from django.db import models
from Game.models import PlayerHand, Deck

class Table(models.Model):

    currentPlayers = []
    isGameRunning = models.BooleanField(default = False)
    playerToPlay = models.IntegerField(default = 0)

    def __init__(self):
        self.__numberOfPlayers = 8
        self.__deck = Deck()
        self.isGameRunning = False
        self.playerToPlay = 0
        for _ in range(self.__numberOfPlayers):
            playerHand = PlayerHand()
            self.currentPlayers.append(playerHand)

    def start_game(self):
        self.isGameRunning = True
        for playerHand in self.currentPlayers:
            playerHand.deal_card(self.__deck.deal_card())
        for playerHand in self.currentPlayers:
            playerHand.deal_card(self.__deck.deal_card())

    def reset_table(self):
        self.__take_hand_from_players()
        self.__deck.shuffle_deck()
        self.isGameRunning = False

    # Used to get the current context of the function
    # in the html
    def get_context(self):
        jsonData = {}
        for index, playerHand in enumerate(self.currentPlayers):
            playerID = "p" + str(index + 1)
            hand = playerHand.get_hand_string()
            jsonData[playerID] = hand
        return jsonData

    # Used as a table reset
    def __take_hand_from_players(self):
        for playerHand in self.currentPlayers:
            playerHand.take_hand_from_player()

    # Moves counter to next player to play
    # also used by table to deal cards
    def move_turn_to_next_player(self):
        self.playerToPlay += 1
        if (self.playerToPlay >= len(self.currentPlayers)):
            self.playerToPlay = 0

    # Returns true if everyone on table has cards
    # otherwise false
    def deal_card(self):
        player = self.currentPlayers[self.playerToPlay]
        player.deal_card(self.__deck.deal_card())
        self.move_turn_to_next_player()