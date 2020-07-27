from classes_file import Deck

players_hand = Deck.deal_hand(Deck)
dealers_hand = Deck.deal_hand(Deck)

print("Welcome to blackjack!")
play = input("Would you like to play? ").upper()
print(f"You've been dealt the following hand: {players_hand[0]}, {players_hand[1]} \nThe Dealer was dealt a: {dealers_hand[1]}")

while play == "YES":
    ply_input = input("Would you like to Hit or Stand? ").upper()

    if ply_input == "HIT":
        Deck.hit(Deck, players_hand)
        if Deck.card_total(Deck, players_hand) > 21:
            print(f"{players_hand} = {Deck.card_total(Deck, players_hand)} Bust! You lose, Dealers hand was {dealers_hand} = {Deck.card_total(Deck, dealers_hand)}")
            break
        print(f"Your current hand is: {players_hand}")
    elif ply_input == "STAND":
       print(Deck.stand(Deck, players_hand, dealers_hand))
       break
