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


def pick_card():
    global played_cards
    random_symbol = random.choice(symbol)
    print(random_symbol)
    random_card = random.choice(cards)
    print(random_card)
    if random_card == "J" or random_card == "Q" or random_card == "K":
        random_card_value = 10
        print(random_card_value)
    if random_card == "A":
        random_card_value = 11
        print(random_card_value)
    picked_card = Card(random_symbol, random_card).get_list()
    print(picked_card)

    global diamond_card
    global club_card
    global heart_card
    global spade_card
    if random_symbol == "Spade":
        print(spade_card)
        if random_card in spade_card:
            spade_card = [x for x in spade_card if x != random_card]
            print(spade_card)

    elif symbol == "Diamond":
        if random_card in diamond_card:
            diamond_card = [x for x in diamond_card if x != random_card]
    elif symbol == "Club":
        if random_card in club_card:
            club_card = [x for x in club_card if x != random_card]
    elif symbol == "Heart":
        if random_card in heart_card:
            heart_card = [x for x in heart_card if x != random_card]
    del picked_card


deal_card = tk.Button(app, text="deal card", command=pick_card)
deal_card.grid(row=0, column=1)


app.mainloop()
