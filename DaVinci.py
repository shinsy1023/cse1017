from module import *
from DCview import *

class DCplayer(Hand):
    @property
    def set_Joker(self, hand):
        super().set_Joker(self, hand)
        while self.joker!=0:
            loc=Reader.select_loc(self, hand)
            #미완

    def result(self, cpu):
        if cpu.card_num==0:
            print("You win!")
            return True
        else:
            print("You lose.")
            return False

class DCcpu(Hand):
    @property

    def __init__(self):
        super().__init__()
        self.ans=[Deck.fresh_deck()]
    
    def set_Joker(self, hand):
        super().set_Joker(self, hand)
        #미완
        
    def correct_ans(self):
        for card in self.ans:
            
