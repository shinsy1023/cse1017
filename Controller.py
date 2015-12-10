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
        while True:
            os.system('clear')
            deck.draw(player, True)
            deck.draw(you)
            print("\n\n\n\n\nDa Vinci : "+str(you), end='')
            print("           ", end='')
            for i in range(len(you.cards)):
                print(str(i+1).rjust(8), end='  ')
            print("\n\n\n\n\n\n\n\n")
            print("My : "+str(player))
            if player.joker!=0 and (player.white_joker==13 or player.black_joker==13):
                print(player.joker)
                player.set_Joker()
            if you.joker!=0:
                you.set_Joker()
            player.sorting(None)
            os.system('clear')
            print("\n\n\n\n\nDa Vinci : "+str(you), end='')
            print("           ", end='')
            for i in range(len(you.cards)):
                print(str(i+1).rjust(8), end='  ')
            print("\n\n\n\n\n\n\n\n")
            print("My : "+str(player))
            while True:
                if you.match(player):
                    os.system('clear')
                    print("\n\n\n\n\nDa Vinci : "+str(you), end='')
                    print("           ", end='')
                    for i in range(len(you.cards)):
                        print(str(i+1).rjust(8), end='  ')
                    print("\n\n\n\n\n\n\n\n")
                    print("My : "+str(player))
                    time.sleep(3)
                    if not Reader.ox("Again? (o/x)"):
                        break
                else:
                    break
            player.match(you.correct_ans(), you)
            time.sleep(3)
            os.system('clear')
            player.sorting(None)
            print("Da Vinci : "+str(you), end='')
            print("           ", end='')
            for i in range(len(you.cards)):
                print(str(i+1).rjust(8), end='  ')
            print("\n\n\n\n\n\n\n\n")
            print("My : "+str(player))
            time.sleep(3)
            player.sorting(None)
            os.system('clear')
            if player.check_win(you):
                print("\n\n\n\n\nDa Vinci : "+str(you), end='')
                print("           ", end='')
                for i in range(len(you.cards)):
                    print(str(i+1).rjust(8), end='  ')
                print("\n\n\n\n\n\n\n\n")
                print("My : "+str(player))
                print("\n\n\n\n\nYou WIN!")
                break
            if player.check_lose():
                print("\n\n\n\n\nDa Vinci : "+str(you), end='')
                print("           ", end='')
                for i in range(len(you.cards)):
                    print(str(i+1).rjust(8), end='  ')
                print("\n\n\n\n\n\n\n\n")
                print("My : "+str(player))
                print("\n\n\n\n\nYou lose.")
                break

def main():
    con=Controller()
    con.play()

main()
