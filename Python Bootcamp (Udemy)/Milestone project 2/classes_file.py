import random

class Deck:


    def __init__(self, cards, hand, total):
        self.cards = self.cards
        self.hand = self.hand
        self.total = self.total
    
    cards = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, "J":10, "Q":10, "K":10, "A":0}

    def deal_hand(self):
        hand_count = 0
        self.hand = []
        while hand_count < 2:
            self.hand.append(random.choice(list(self.cards)))
            hand_count += 1
        if hand_count == 2:
            return self.hand

    
    def card_total(self, players_hand):
        self.total = 0
        for card in players_hand:
        #     if card == "A":
        #         card = input("You have an ace in your hand, do you wish to play it as a 1 or 11?: ")
        #         print(f"Ace is now being played as a(n) {card}")
        #         self.total += int(card)
        #     else:
            self.total += self.cards[card]
        return self.total


    def hit(self, hand):
        return hand.append(random.choice(list(self.cards)))

    # Does not handle a matching 21 and 21 or if the player wins yet
    def stand(self, players_hand, dealers_hand):
        player_total = Deck.card_total(Deck, players_hand)
        print(f"Your hand total is: {player_total}")
        if Deck.card_total(Deck, dealers_hand) < player_total:
            while Deck.card_total(Deck, dealers_hand) < player_total:
                Deck.hit(Deck, dealers_hand)
                if Deck.card_total(Deck, dealers_hand) > 21:
                    print(f'Dealer busts with: {Deck.card_total(Deck, dealers_hand)}')
                    break
        elif Deck.card_total(Deck, dealers_hand) > player_total:
            print(f"Players total was: {player_total} and the Dealer had {Deck.card_total(Deck, dealers_hand)}")
            print("Dealer Wins!")