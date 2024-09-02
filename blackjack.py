import random
card_categories = ["hearts", "diamonds", "clubs", "spades"]
cards_list = ['Ace', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
              'jack', 'queen', 'king']
deck = [(card, category) for category in card_categories for card in cards_list]

def card_value(card):
    if card[0] in ['jack', 'queen', 'king']:
        return 10
    elif card[0] == 'Ace':
        return 11
    else:
        return int(card[0])

random.shuffle(deck)
player_card = [deck.pop(), deck.pop()]
dealer_card = [deck.pop(), deck.pop()]

while True:
    player_score = sum(card_value(card) for card in player_card)
    dealer_score = sum(card_value(card) for card in player_card)
    print("Cards the player has:", player_card)
    print("Score of the player:", player_score)
    print("/n")
    choice  = input("What do you want to do? [\"play\" to request another card, \"Stop\" to stop]: ").lower()
    if choice == "play":
        new_card = deck.pop()
        player_card.append(new_card)
    elif choice == "stop":
            break
    else:        
        print("Invalid choice, please try again.")
        continue
    if player_score > 21:
        print("The ddealer has: ", dealer_card)
        print("The dealer score  is: ", dealer_score)
        print("Player card is: ", player_card)
        print("Score of the player is: ", player_score)
        print("Dealer wins beacuse player cards are over 21")
        break

    while dealer_score < 17:
        new_card = deck.pop()
        dealer_card.append(new_card)
        dealer_score += card_value(new_card)
    print("Cards the dealer has: ", dealer_card )
    print("Score of the dealer: ", dealer_score)
    print("\n")

    if dealer_score > 21:
        print("Cards dealer has: ", dealer_card)
        print("Score of the dealer: ", dealer_score)
        print("Player cards are: ", player_card)
        print("Player score  is :", player_score)
        print("Dealer loses because his total of his card are greater than 21")
    elif player_score > dealer_score:
        print("Cards dealer has: ", dealer_card)
        print("Score of the dealer: ", dealer_score)
        print("Player cards are: ", player_card)
        print("Player score  is :", player_score)
        print("Player wins because his cards are closer to 21 than the dealer's!")
    elif player_score == dealer_score:
        print("Cards dealer has: ", dealer_card)
        print("Score of the dealer: ", dealer_score)
        print("Player cards are: ", player_card)
        print("Player score  is :", player_score)
        print("Dealer and player have the same card score, it is a tie!")
        
        
            
        
    
        
        
