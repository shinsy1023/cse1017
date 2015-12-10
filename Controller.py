from DaVinci import *
from module import *
import os
import time

class Controller(object):
    def play(self):
        show=""
        os.system('clear')
        print("Welcome to Da Vinci World!")
        print("==========================")
        deck=Deck()
        deck.fresh_deck()
        player=DCplayer()
        you=DCcpu(deck.cards)
        for _ in range(5):
            deck.draw(player, True)
            deck.draw(you)
        os.system('clear')
        print("Da Vinci : "+str(you))
        print("\n\n\n\n\n\n\n\n")
        print("My : "+str(player))
        you.set_Joker()
        player.set_Joker()
        time.sleep(3)
        while True:
            os.system('clear')
            deck.draw(player, True)
            deck.draw(you)
            if player.joker!=0:
                player.set_Joker()
            if you.joker!=0:
                you.set_Joker()
            print("Da Vinci : "+str(you))
            print("\n\n\n\n\n\n\n\n")
            print("My : "+str(player))
            you.match(player)
            # import random
            # time.sleep(random.randrange(2,6))
            player.match(you.correct_ans(), you)
            os.system('clear')
            print("Da Vinci : "+str(you))
            print("\n\n\n\n\n\n\n\n")
            print("My : "+str(player))
            time.sleep(3)

def main():
    con=Controller()
    con.play()

main()
