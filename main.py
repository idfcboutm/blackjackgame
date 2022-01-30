import tkinter as tk
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
import random
from cards import cards, symbol, played_cards

app = tk.Tk()
app.title("Blackjack")


class Karte:
    def __init__(self, value, symbol):
        self.value = value
        self.symbol = symbol


def pick_card():
    global cards
    global symbol
    random_card = random.choice(cards)
    random_symbol = random.choice(symbol)
    print(random_card)
    print(random_symbol)
    add_card(random_card, random_symbol)


def add_card(card, symbol):
    global played_cards
    card_played = []

    played_cards = played_cards.append(card)
    return played_cards


pick_card()
print(played_cards)

app.mainloop()
