from module import *
from DCview import *

class DCplayer(Hand):
    def __init__(self):
        super(DCplayer, self).__init__()
        self.check_correct=[]

    def __str__(self):
        show=super(DCplayer, self).__str__()
        show+="    "
        for check in self.check_correct:
            show+=check.rjust(8)+"  "
        return show

    def set_Joker(self):
        left=[]
        right=[]
        while self.joker!=0:
            loc=Reader.select_loc(self, self)
            if self.cards[len(self.cards)-1].color=="White":
                self.white_joker=loc
            else:
                self.black_joker=loc
            left=self.cards[:loc-1]
            right=self.cards[loc-1:]
            left.append(self.cards[len(self.cards)-self.joker])
            right.remove(self.cards[len(self.cards)-self.joker])
            self.cards=left+right
            self.joker=self.joker-1

    def match(self, card, you):
        num=0
        import random
        while True:
            print("match")
            num=random.randrange(len(self.cards))
            if self.check_correct[num]=="Covered":
                break
        if self.cards[num-1]==card:
            print("right")
            self.cards[self.cards.index(card)].check=1
        else:
            print("wrong")
            you.wrong()

    def status(self):
        for i in range(len(self.cards)):
            if self.cards[i].check==0:
                self.check_correct[i]="Covered"
            else:
                self.check_correct[i]="Opened"

    def sorting(self, card):
        super(DCplayer, self).sorting(card)
        for i in range(len(self.cards)):
            self.check_correct[i]=" "
        self.status()


    def check_win(self, you):
        count=0
        for card in you.cards:
            if card.face_up:
                count+=1
        if count==len(you.cards):
            self.win()
            return True

    def check_lose(self):
        count=0
        for card in self.cards:
            if card.check==1:
                count+=1
        if count==len(self.cards):
            self.lose()
            return True

    def wrong(self):
        print("You wrong!")
        loc=Reader.select_loc(self, self)
        while True:
            if self.check_correct[loc-1]=="Covered":
                self.cards[loc-1].check=1
                break
            else:
                loc=Reader.select_loc(self, self)

class DCcpu(Hand):
    def __init__(self, cards):
        super(DCcpu, self).__init__()
        self.ans=cards
        self.check_correct=[]

    def choose_loc(self):#조커 위치
        loc=0
        for i in range(len(self.cards)-1):
            if int(self.cards[i+1].number)-int(self.cards[i].number)>3:
                return i
            elif int(self.cards[i+1].number)-int(self.cards[i].number)==0:
                import random
                return i+1
            else:
                import random
                loc=random.randrange(2)
                if loc==0:
                    return 1
                else:
                    return len(self.cards)-1

    def set_Joker(self):
        left=[]
        right=[]
        while self.joker!=0:
            loc=self.choose_loc()
            if self.cards[len(self.cards)-1].color=="White":
                self.white_joker=loc
            else:
                self.black_joker=loc
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
        return self.ans[random.randrange(len(self.ans))]

    def wrong(self):
        while True:
            import random
            loc=random.randrange(len(self.cards))
            if not self.cards[loc].face_up:
                self.cards[loc].flip()
                break