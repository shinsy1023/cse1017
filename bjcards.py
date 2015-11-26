# Playing Cards for Blackjack
from cards import *
from view import *

class BJCard(Card):
    @property
    def value(self):
        v = BJCard.RANKS.index(self.rank) + 1
        if v > 10:
            v = 10
        return v

class BJDeck(Deck):
    def fresh_deck(self):
        for s in BJCard.SUITS:
            for r in BJCard.RANKS:
                self.cards.append(BJCard(s,r,False))
        import random
        random.shuffle(self.cards)

class BJHand(Hand):
    def __init__(self,name):
        super(BJHand,self).__init__()
        self.name = name
    
    def __str__(self):
        if len(self.cards) == 0:
            show = "empty"
        else:
            show = ""
            for card in self.cards:
                show += str(card) + " "
        return show

    @property
    def total(self):
        point = 0
        number_of_ace = 0
        for card in self.cards:
            if card.rank == 'A':
                point += 11
                number_of_ace += 1
            else:
                point += card.value
        while point > 21 and number_of_ace > 0:
            point -= 10
            number_of_ace -= 1
        return point
    
    def open(self):
        for card in self.cards:
            card.face_up = True
            
    def busted(self):
        return self.total > 21
    
    def blackjack(self):
        return self.total == 21
            
class BJPlayer(BJHand):
    def __init__(self, name):
        super(BJPlayer,self).__init__(name)
        self.chips = 0
        self.wins = 0
        
    def hit(self):
        return self.total < 21 and \
               Reader.ox(self.name + ": Hit?(o/x) ")
        
    def bust(self):
        self.wins -= 1
        self.chips -= 1
        print(self.name,"busts.")
    
    def lose(self):
        self.wins -= 1
        self.chips -= 1
        print(self.name,"loses.")
    
    def win(self,n):
        self.wins += 1
        self.chips += n
        print(self.name,"wins.")

    def draw(self):
        self.wins += 0.5
        print(self.name,"draws.")
        
    def print_chips(self):
        print(self.name, "has", self.chips, "chips.")

class BJDealer(BJHand):
    def hit(self):
        return self.total <= 16
        
    def bust(self):
        print(self.name,"busts.")

