import random
def deck_of_cards():
    suit = ["CLUBS", "DIAMONDS", "HEARTS", "SPADES"]
    rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "JACK", "QUEEN", "KING", "ACE"]
    cards = []

    for i in range(4):
        a = []
        for j in range(9):
            card = random.choice(rank) + " " + random.choice(suit)
            a.append(card)
        cards.append(a)

    for i in cards:
        for j in i:
            print("{0}".format(j),end=", ")
        print()

if __name__ == '__main__':
    deck_of_cards()




