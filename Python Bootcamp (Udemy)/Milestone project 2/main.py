from classes_file import Deck

print("Welcome to blackjack!")

players_hand = Deck.deal_hand(Deck)
dealers_hand = Deck.deal_hand(Deck)

print(f"You've been dealt the following hand: {players_hand[0]}, {players_hand[1]} \nThe Dealer was dealt a: {dealers_hand[1]}")

while Deck.card_total(Deck, players_hand) <= 21:
    print(f"Current hand total is: {Deck.card_total(Deck, players_hand)}")
    ply_input = input("Would you like to Hit or Stand? ").upper()

    if ply_input == "HIT":
        print("Player hits")
        Deck.hit(Deck, players_hand)
        if Deck.card_total(Deck, players_hand) > 21:
            print(f"{Deck.card_total(Deck, players_hand)} Bust! You lose")
            break
        print(f"Your current hand is: {players_hand}")
        continue
    elif ply_input == "STAND":
        Deck.stand(Deck, players_hand, dealers_hand)
        # Need to handle break and more verbose output of cards to ensure proper totals are being calculated for winnig
