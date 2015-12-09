class Card(object):
    COLORS=["White", "Black"]
    NUMBERS=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "-"]

    def __init__(self, color, number, face_up=False):
        if color in Card.COLORS and number in Card.NUMBERS:
            self.color=color
            self.number=number
            self.face_up=face_up
        else:
            print("Error : Not a right color or number")

    def __str__(self):
        if self.face_up:
            return self.color+self.number.rjust(3)+" "
        else:
            return "XXXXX"
        
    def flip(self):
        self.face_up=not self.face_up

class Hand(object):
    def __init__(self):
        self.cards=[]

    def __str__(self):
        if len(self.cards) == 0:
            show = "empty"
        else:
            show = ""
            for card in self.cards:
                show += str(card) + " "
        return show
        
    def clear(self):
        self.cards=[]

    def add(self, card):
        self.cards.append(card)

    def give(self, card, hand):
        self.cards.remove(card)
        hand.add(card)

    def match(self, card, hand):
        if card in hand.cards:
            hand.cards[hand.index(card)].flip()

    def set_Joker(self, hand):
        self.joker=0
        for card in hand.cards:
            if card=="-":
                self.joker+=1
                
class Deck(Hand):
    def fresh_deck(self):
        self.cards = []
        for s in Card.COLORS:
            for r in Card.NUMBERS:
                self.cards.append(Card(s,r,False))
        import random
        random.shuffle(self.cards)
        
    def draw(self, hand, how_many=1, open=False):
        if self.cards == []:
            self.fresh_deck()
        for _ in range(how_many):
            card = self.cards[0]
            if open :
                card.flip()
            self.give(card,hand)
