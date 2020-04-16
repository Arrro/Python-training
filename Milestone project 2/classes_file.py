import random

class Deck:


    def __init__(self, cards, hand, total):
        self.cards = self.cards
        self.hand = self.hand
        self.total = self.total
    
    cards = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, "J":10, "Q":10, "K":10, "A":0}

    def player_hand(self):
        hand_count = 0
        self.hand = []
        while hand_count < 2:
            self.hand.append(random.choice(list(self.cards)))
            hand_count += 1
        if hand_count is 2:
            return self.hand

    
    def card_total(self):
        self.total = 0
        for card in self.hand:
            self.total += self.cards[card]
        return self.total


    def hit(self, hand: list):
        return self.hand.append(random.choice(self.cards))
        #for card in self.hand:
            #if card is "A":
            #    card = input("You have an ace in your hand, do you wish to play it as a 1 or 11?: ")
            #    self.total += int(card)