from module import *
from DCview import *

class DCplayer(Hand):
    def __init__(self):
        super(DCplayer, self).__init__()
        self.check_correct=[0, 0, 0, 0, 0]

    def __str__(self):
        super(DCplayer, self).__str__()
        for card in self.cards:
            if card.face_up:


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

    def match(self, card, you):
        if card in self.cards:
            self.check_correct[self.cards.index(card)]=1
        else:
            you.wrong()


class DCcpu(Hand):
    @property
    def __init__(self):
        super(DCcpu, self).__init__()
        self.ans=[deck.cards]

    def choose_loc(self):
        loc=0
        for i in range(len(self.cards)-1):
            if self.cards[i+1].number-self.cards[i].number>3:
                return i
            elif self.cards[i+1].number-self.cards[i].number==0:
                import random
                return i+1
            else:
                loc=random.randrange(2)
                if loc==0:
                    return 1
                else:
                    return len(self.cards)-1

    def set_Joker(self, hand):
        left=[]
        right=[]
        while self.joker!=0:
            loc=self.choose_loc()
            left=self.cards[:loc-1]
            right=self.cards[loc-1:]
            left.append(self.cards[len(self.cards)-self.joker])
            right.remove(self.cards[len(self.cards)-self.joker])
            self.cards=left+right
            self.joker=self.joker-1
        
    def correct_ans(self):
        for i in range(len(self.cards)):
            for j in range(len(self.ans)):
                if self.cards[i].color==self.ans[j].color\
                        and self.cards[i].number==self.ans[j].number:
                    self.ans.remove(self.ans[j])
                    break
        import random
        return ans[random.randrange(len(ans))]

    def wrong(self):
        while True:
            import random
            loc=random.randrange(len(self.cards))
            if not self.cards[loc].face_up:
                self.cards[loc].flip()

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
