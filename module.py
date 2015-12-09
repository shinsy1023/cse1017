class Card(object):
    COLORS=["White", "Black"]
    NUMBERS=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]

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
            if card=="13":
                self.joker+=1

    def win(self):
        print("You win!")
        
    def lose (self):
        print("You lose!")

    def open(self):
        for card in self.cards:
            card.face_up=True

    def sorting(self):
        sort=[]
        num_list=[]
        all_card=self.cards
        num=14
        for i in range(len(self.cards)):
            num=int(self.cards[i].number)
            num_list.append(num)
        num_list.sort()
        for i in range(len(self.cards)):
            for j in range(len(self.cards)):
                if all_card[j].number==str(num_list[i]):
                    sort.append(all_card[j])
                    all_card.remove(all_card[j])
                    break
        self.cards=sort
                
class Deck(Hand):
    def fresh_deck(self):
        self.cards = []
        for s in Card.COLORS:
            for r in Card.NUMBERS:
                self.cards.append(Card(s,r,False))
        import random
        random.shuffle(self.cards)
        
    def draw(self, hand, open=False):
        if self.cards == []:
            self.fresh_deck()
        card = self.cards[0]
        if open :
            card.flip()
        self.give(card,hand)

deck=Deck()
deck.fresh_deck()
hand=Hand()
print(hand)
for _ in range(5):
    deck.draw(hand)
print(hand)
hand.open()
print(hand)
hand.sorting()
print(hand)
# hand.cards.sort()
# print(hand)
