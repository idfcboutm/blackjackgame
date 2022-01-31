import tkinter as tk
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
import random
from cards import cards, symbol, played_cards, spade_card, heart_card, diamond_card, club_card

app = tk.Tk()
app.title("Blackjack")


class Card:
    def __init__(self, symbol, value):
        self.symbol = symbol
        self.value = value

    def get_list(self):
        return [self.symbol, self.value]


# picking a random card as well as a random symbol
def pick_card():
    global played_cards
    random_symbol = random.choice(symbol)
    random_card = random.choice(cards)
    print("This is the random card dealead " + str(random_card))

    if random_card == "J" or random_card == "Q" or random_card == "K":
        picked_card = Card(random_symbol, random_card).get_list()
        random_card_value = 10
        check_card(random_symbol, random_card, picked_card, random_card_value)

    elif random_card == "A":
        picked_card = Card(random_symbol, random_card).get_list()
        random_card_value = 11
        check_card(random_symbol, random_card, picked_card, random_card_value)

    else:
        picked_card = Card(random_symbol, random_card).get_list()
        random_card_value = int(random_card)
        check_card(random_symbol, random_card, picked_card, random_card_value)


# check if card was already played
def check_card(random_symbol, random_card, picked_card, random_card_value):
    global diamond_card
    global club_card
    global heart_card
    global spade_card

    if random_symbol == "Spade":
        if random_card in spade_card:
            spade_card = [x for x in spade_card if x != random_card]
            print("This is the picked Card" + str(picked_card))
            card_count(random_card_value)
        else:
            print_already_dealed()
            pick_card()

    elif random_symbol == "Diamond":
        if random_card in diamond_card:
            diamond_card = [x for x in diamond_card if x != random_card]
            print("This is the picked Card" + str(picked_card))
            card_count(random_card_value)
        else:
            print_already_dealed()
            pick_card()

    elif random_symbol == "Club":
        if random_card in club_card:
            club_card = [x for x in club_card if x != random_card]
            print("This is the picked Card" + str(picked_card))
            card_count(random_card_value)
        else:
            print_already_dealed()
            pick_card()

    elif random_symbol == "Heart":
        if random_card in heart_card:
            heart_card = [x for x in heart_card if x != random_card]
            print("This is the picked Card" + str(picked_card))
            card_count(random_card_value)
        else:
            print_already_dealed()
            pick_card()


# printing a statement
def print_already_dealed():
    print("Card was already dealed. Picking another one")


# shuffeling cards
def shuffle():
    global diamond_card
    global club_card
    global heart_card
    global spade_card
    spade_card = cards
    heart_card = cards
    diamond_card = cards
    club_card = cards


# counting the whole value a player has on his hand
card_counted = 0


def card_count(value):
    global card_counted
    value = int(value)
    card_counted += value
    print("This is the card_count: " + str(card_counted))
    if card_counted > 21:
        print("You lost!")
        card_counted = 0
    print("")


deal_card_btn = tk.Button(app, text="deal card", command=pick_card)
deal_card_btn.grid(row=0, column=1)
shuffle_btn = tk.Button(app, text="Shuffle", command=shuffle)
shuffle_btn.grid(row=1, column=1)

app.mainloop()
