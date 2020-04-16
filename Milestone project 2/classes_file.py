import random

class Deck:


    def __init__(self, cards):
        self.cards = self.cards
    
    cards = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, "J":10, "Q":10, "K":10, "A":0}

    def player_hand(self):
        hand_count = 0
        hand = []
        while hand_count < 2:
            hand.append(random.choice(list(self.cards)))
            hand_count += 1
        if hand_count is 2:
            return hand

    def hit(self, hand: list):
        total = 0
        for card in hand:
            if card is "A":
                card = input("Dealer has dealt an Ace, would like to play it as a 1 or 11?: ")
                total += int(card)
            else:
                total += self.cards[card]
        return total
