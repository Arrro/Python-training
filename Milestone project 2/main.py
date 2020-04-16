from classes_file import Deck

players_hand = Deck.player_hand(Deck)
hit = Deck.hit(Deck, players_hand)

player_1 = input(f"welcome to blackjack, youve been dealt the following hand: {players_hand} would you like to hit or fold?").upper()

print(players_hand)
print(Deck.card_total(Deck))

if player_1 is "YES":
    print(Deck.hit(Deck, players_hand))
