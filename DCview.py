class Reader(object):
    def select_loc(self, hand):
        loc=input("Select number where you want.")
        while True:
            if loc.isdigit() and len(hand.cards)>=int(loc):
                break
            else:
                loc=input("Select number where you want.")
        return int(loc)

    #def type_hard(self):
     #   hard=input("Type the level of difficulty you want.")
      #  return hard

    def get_number():
        num=input("Type the number.")
        while True:
            if num.isdigit():
                break
            else:
                num=input("Type the number.")
        return num
