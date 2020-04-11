# blackjack 0.1v
# ace value if fixed = 11
import random as rr
class computer():

    def __init__(self,cards1,a,sum):
        self.cards1 = cards1
        self.a = a
        self.sum = sum
    def display(self):
        print('DEALER')
        for i in range(self.a):
            print(self.cards1[i],end=' ')
        print()
    def calc(self):
        ace = 11
        self.sum = 0
        for i in range(self.a):
            if (self.cards1[i] == 'two'):
                self.sum = self.sum + 2
            elif (self.cards1[i] == 'three'):
                self.sum = self.sum + 3
            elif (self.cards1[i] == 'four'):
                self.sum = self.sum + 4
            elif (self.cards1[i] == 'five'):
                self.sum = self.sum + 5
            elif (self.cards1[i] == 'six'):
                self.sum = self.sum + 6
            elif (self.cards1[i] == 'seven'):
                self.sum = self.sum + 7
            elif (self.cards1[i] == 'eigth'):
                self.sum = self.sum + 8
            elif (self.cards1[i] == 'nine'):
                self.sum = self.sum + 9
            elif (self.cards1[i] == 'ten') or (self.cards1[i] == 'jack') or (self.cards1[i] == 'queen') or (self.cards1[i] == 'king'):
                self.sum = self.sum + 10
            elif (self.cards1[i] == 'ace'):
                self.sum = self.sum + ace

class human():

    def __init__(self,cards2,b,sum):
        self.cards2 = cards2
        self.b = b
        self.sum =  sum
    def display(self):
        print('HUMAN')
        for i in  range(self.b):
            print(self.cards2[i],end=' ')
        print()
    def calc(self):
        ace  = 11
        self.sum = 0
        for i in range(0,self.b):
            if (self.cards2[i] == 'two'):
                self.sum = self.sum + 2
            elif (self.cards2[i] == 'three'):
                self.sum = self.sum + 3
            elif (self.cards2[i] == 'four'):
                self.sum = self.sum + 4
            elif (self.cards2[i] == 'five'):
                self.sum = self.sum + 5
            elif (self.cards2[i] == 'six'):
                self.sum = self.sum + 6
            elif (self.cards2[i] == 'seven'):
                self.sum = self.sum + 7
            elif (self.cards2[i] == 'eigth'):
                self.sum = self.sum + 8
            elif (self.cards2[i] == 'nine'):
                self.sum = self.sum + 9
            elif (self.cards2[i] == 'ten') or (self.cards2[i] == 'jack') or (self.cards2[i] == 'queen') or (self.cards2[i] == 'king'):
                self.sum = self.sum + 10
            elif (self.cards2[i] == 'ace'):
                self.sum = self.sum + ace

def dealer_call():
    while True:
        c.a = c.a + 1
        c.display()
        c.calc()
        if (c.sum > 21):
            print('DEALER BUST!')
            return True
        elif (c.sum > h.sum):
            print("DEALER WIN!")
            return True
        elif (c.sum < h.sum):
            continue
        else:
            print('DEALER WIN!')
            return True            
#__main__
cards_c = ["two","three",'four','five','six','seven','eigth','nine','ten','jack','queen','king','ace']*2
cards_h = ["two","three",'four','five','six','seven','eigth','nine','ten','jack','queen','king','ace']*2
rr.shuffle(cards_c)
rr.shuffle(cards_h)
a,b = 1,2
fixed_bet = 100
s = 0
s1 = 0
print(f"Having bet:{fixed_bet}")
bet = int(input("bet:"))
c = computer(cards_c,a,s1)
h = human(cards_h,b,s)
c.display()
print('\n')
h.display()
while True:
    h.calc()
    #print(h.sum)
    if  (h.sum > 21):
        print('HUMAN BUST!')
        break
    elif (h.sum < 21):
        option = input('hit(h) stay(s)\n')
        if option == 'h':
            h.b = h.b + 1
            h.display()
        else:
            xx = dealer_call()
            if xx:
                break

    elif (h.sum == 21):
        print('HUMAN WON!')
        break
    