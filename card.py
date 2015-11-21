class Card(object):
    SUITS=["Dioamond", "Heart", "Spacde", "Clover"]
    RANKS=["A", "2", "3", "4", "5", "6", "7", "8", "8", "10",
           "J", "Q", "K"]

    def __init__(self, suit, rank, face_up=True):
        if suit in Card.SUITS and rank in Card.RANKS:
            self.suit=suit
            self.rank=rank
            self.face_up=face_up
        else:
            print("Error: Not a right suit or rank")

    def __str__(self):
        if self.face_up:
            return self.suit+self.rank
        else:
            return "XXXXX"

    def flip(self):
        self.face_up=not self.face_up

import random
hand=[]
for _ in range(5):
    suit=random.choice(Card.SUITS)
    rank=random.choice(Card.RANKS)
    hand.append(Card(suit, rank, False))
hand[0].flip()
hand[1].flip()
for c in hand:
    print(c)
