from module import *
from DCview import *

class DCplayer(Hand):
    @property
    def set_Joker(self):
        left=[]
        right=[]
        while self.joker!=0:
            loc=Reader.select_loc(self, hand)
            left=self.cards[:loc-1]
            right=self.cards[loc-1:]
            left.append(self.cards[len(self.cards)-self.joker])
            right.remove(self.cards[len(self.cards)-self.joker])
            self.cards=left+right
            self.joker=self.joker-1
            print(self)

class DCcpu(Hand):
    @property
    def __init__(self):
        super().__init__()
        self.ans=[Deck.fresh_deck()]
    
    def set_Joker(self, hand):
        
        #미완
        
    # def correct_ans(self):
    #     for card in self.ans:


deck=Deck()
deck.fresh_deck()
hand=DCplayer()
print(hand)
for _ in range(5):
    deck.draw(hand)
print(hand)
hand.open()
print(hand)
hand.sorting()
print(hand)
if hand.joker!=0:
    hand.set_Joker
print(hand)
# hand.cards.sort()
# print(hand)
