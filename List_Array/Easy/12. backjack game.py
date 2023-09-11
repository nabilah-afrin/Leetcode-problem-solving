def deal_cards():
    #return a random card
    import random
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    random.choice(cards)
    return cards
user_card = []
dealer_card = []
for _ in range(2):
    user_card.append(deal_cards())
    dealer_card.append(deal_cards())
def calculate_cards(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0