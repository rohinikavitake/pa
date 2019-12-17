import random
suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
value = {'Two': 2,'Three' : 3,'Four' :4,'Five':5,'Six':6,'seven' :7,'Eight' :8,'Nine' :9,'Ten' :10,'jack':10,'Queen' :10,'King' :10,'Ace' :10,}

playing=True

# CLASS DEFINITIONS
class Card:
    def __init__(self, suit, rank):
        self.suits = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:

    def __init__(self):
        self.deck = [] #start with an empty list

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp ='' #start with an empty string

        for card in self.deck:
            deck_comp += '\n' + card.__str__() #add each card object print string
            return  'The deck has:' + deck_comp

    def deal(self):
        single_card =self.deck.opo()
        return single_card

class Hand:

    def __init__(self):
        self.card = [] #start with an empty list as we did in the Deck class
        self.value = 0 #start with zero value
        self.aces = 0 #add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank =='Ace':
            self.aces += 1 #add to self.aces

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

#FUNCTION DEFINITIONS:
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('Hwo many chips would you like to bet? '))
        except ValueError:
            print("Sorry, your bet can't exceed",chips.total)
        else:
            break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing

    while True:
        x= input("Would you like to Hit or Stand? Enter 'h' or 's' ")

        if x[0].lower() =='s':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again")
            break

def show_some(player, dealer):
   print("\nDelar's Hand:")
   print(" <vard hidden>")
   print("\nPlayer's Hand:",player.cards[1])
   print("\nPlayer's Hand:",*player.cards,sep='\n ')

def show_all(player,dealer):
    print()








