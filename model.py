class Card(object):
    COLORS=["White", "Black"]
    NUMBERS=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "-"]

    def __init__(self, color, number, face_up=True):
        if color in Card.COLORS and number in Card.NUMBERS:
            self.color=color
            self.number=number
            self.face_up=face_up
        else:
            print("Error : Not a right color or number")

    def __str__(self):
        if self.face_up:
            return self.color+"\n"+self.number.rjust(5)
        else:
            return "XXXXX"+"\n"+"XX".rjust(5)
        
    def flip(self):
        self.face_up=not self.face_up

class Hand(object):
    def __init__(self):
        self.cards=[]

    def clear(self):
        self.cards=[]

    def add(self, card):
        self.cards.append(card)

    def give(self, card, hand):
        self.cards.remove(card)
        hand.add(card)
