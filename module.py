from DCview import *

class Card(object):
    COLORS=["White", "Black"]
    NUMBERS=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]

    def __init__(self, color, number, face_up=False):
        if color in Card.COLORS and number in Card.NUMBERS:
            self.color=color
            self.number=number
            self.face_up=face_up
            self.check=0
        else:
            print("Error : Not a right color or number")

    def __str__(self):
        if self.face_up:
            if self.number!="13":
                return self.color+self.number.rjust(3)+" "
            else:
                return self.color+"-".rjust(3)+" "
        else:
            return self.color+" XX "
        
    def flip(self):
        self.face_up=not self.face_up

class Hand(object):
    def __init__(self):
        self.cards=[]
        self.joker=0
        self.white_joker=13
        self.black_joker=13

    def __str__(self):
        if len(self.cards) == 0:
            show = "empty"
        else:
            show = ""
            for i in range(len(self.cards)):
                show += str(self.cards[i]) + " "
            show+="\n"
        return show
        
    def clear(self):
        self.cards=[]

    def add(self, card):
        self.cards.append(card)

    def give(self, card, hand):
        self.cards.remove(card)
        hand.add(card)

    def match(self, player):
        loc=Reader.select_loc(self, self)
        num=Reader.get_number()
        if num==self.cards[loc-1].number:
            self.cards[loc-1].flip()
        else:
            player.wrong()

    def win(self):
        print("You win!")
        
    def lose (self):
        print("You lose!")

    def open(self):
        for card in self.cards:
            card.face_up=True

    def sorting(self, card):
        sort=[]
        new_loc=0
        num_list=[]
        left=[]
        right=[]
        all_card=self.cards
        num=14
        for i in range(len(self.cards)):
            num=int(self.cards[i].number)
            if num==13 and (self.white_joker==13 or self.black_joker==13):
                if len(self.cards)>4:
                    self.joker+=1
            num_list.append(num)
        num_list.sort()
        for i in range(len(self.cards)):
            for j in range(len(self.cards)):
                if all_card[j].number==str(num_list[i]):
                    sort.append(all_card[j])
                    if all_card[j]==card:
                        new_loc=i
                    all_card.remove(all_card[j])
                    break
        for i in range(len(sort)-1):
            if sort[i].number==sort[i+1].number:
                if sort[i].color=="White":
                    sort[i], sort[i+1]=sort[i+1], sort[i]
        if self.white_joker!=13:
            if self.white_joker<i:
                left=sort[:self.white_joker-1]
                right=sort[self.white_joker-1:]
                left.append(sort[len(sort)-1])
                right.remove(sort[len(sort)-1])
                sort=left+right
            else:
                left=sort[:self.white_joker]
                right=sort[self.white_joker:]
                left.append(sort[len(sort)-1])
                right.remove(sort[len(sort)-1])
                sort=left+right
        if self.black_joker!=13:
            if self.black_joker<i:
                left=sort[:self.black_joker-1]
                right=sort[self.black_joker-1:]
                left.append(sort[len(sort)-1])
                right.remove(sort[len(sort)-1])
                sort=left+right
            else:
                left=sort[:self.black_joker-1]
                right=sort[self.black_joker-1:]
                left.append(sort[len(sort)-1])
                right.remove(sort[len(sort)-1])
                sort=left+right
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
        hand.check_correct.append(".")
        if self.cards != []:
            card = self.cards[0]
            if open :
                card.flip()
            self.give(card,hand)
        hand.sorting(card)