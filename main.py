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


# start the game --> deals more cards
def start_game():
    player_count = int(input("Bitte Spieleranzahl angeben"))
    i = 0
    k = 0
    dealer_number = player_count + 1
    dealer_second_card = dealer_number*2
    while i <= player_count*2+1:
        i += 1
        k += 1
        print(i)
        if i == dealer_number or i == dealer_second_card:
            pick_card_dealer()
            k = 0
        else:
            print("Player: " + str(k))
            pick_card()


# picking a random card as well as a random symbol
def pick_card():
    global played_cards
    random_symbol = random.choice(symbol)
    random_card = random.choice(cards)
    print("This is the random card dealead  to the player: " + str(random_card))
    if random_card == "J" or random_card == "Q" or random_card == "K":
        picked_card = Card(random_symbol, random_card).get_list()
        random_card_value = int(10)
        check_card(random_symbol, random_card, picked_card, random_card_value)
    elif random_card == "A":
        picked_card = Card(random_symbol, random_card).get_list()
        random_card_value = int(11)
        check_card(random_symbol, random_card, picked_card, random_card_value)
    else:
        picked_card = Card(random_symbol, random_card).get_list()
        random_card_value = int(random_card)
        check_card(random_symbol, random_card, picked_card, random_card_value)


# picking dealer card
def pick_card_dealer():
    global played_cards
    random_symbol = random.choice(symbol)
    random_card = random.choice(cards)
    print("This is the random card dealead for the dealer: " + str(random_card))

    if random_card == "J" or random_card == "Q" or random_card == "K":
        picked_card = Card(random_symbol, random_card).get_list()
        random_card_value = 10
        check_card_dealer(random_symbol, random_card,
                          picked_card, random_card_value)

    elif random_card == "A":
        picked_card = Card(random_symbol, random_card).get_list()
        random_card_value = 11
        check_card_dealer(random_symbol, random_card,
                          picked_card, random_card_value)

    else:
        picked_card = Card(random_symbol, random_card).get_list()
        random_card_value = int(random_card)
        check_card_dealer(random_symbol, random_card,
                          picked_card, random_card_value)

# check if card was already played


def check_card(random_symbol, random_card, picked_card, random_card_value):
    global diamond_card
    global club_card
    global heart_card
    global spade_card

    if random_symbol == "Spade":
        card_deal(random_card, spade_card, picked_card,
                  random_card_value, random_symbol)
    elif random_symbol == "Diamond":
        card_deal(random_card, diamond_card,
                  picked_card, random_card_value, random_symbol)
    elif random_symbol == "Club":
        card_deal(random_card, club_card, picked_card,
                  random_card_value, random_symbol)
    elif random_symbol == "Heart":
        card_deal(random_card, heart_card, picked_card,
                  random_card_value, random_symbol)


def card_deal(random_card, list_given, picked_card, random_card_value, random_symbol):
    global spade_card
    global heart_card
    global club_card
    global diamond_card
    if random_card in list_given:
        list_given = [x for x in list_given if x != random_card]
        print_picked_card(picked_card)
        card_count(random_card_value)
        if random_symbol == "Spade":
            spade_card = list_given
            print(spade_card)
        elif random_symbol == "Club":
            club_card = list_given
            print(club_card)
        elif random_symbol == "Diamond":
            diamond_card = list_given
            print(diamond_card)
        elif random_symbol == "Heart":
            heart_card = list_given
            print(heart_card)
    else:
        print_already_dealed()
        pick_card()


def check_card_dealer(random_symbol, random_card, picked_card, random_card_value):
    global diamond_card
    global club_card
    global heart_card
    global spade_card
    if random_symbol == "Spade":
        spade_card = card_deal_dealer(
            random_card, spade_card, picked_card, random_card_value, random_symbol)

    elif random_symbol == "Diamond":
        diamond_card = card_deal_dealer(
            random_card, diamond_card, picked_card, random_card_value, random_symbol)
    elif random_symbol == "Club":
        club_card = card_deal_dealer(
            random_card, club_card, picked_card, random_card_value, random_symbol)

    elif random_symbol == "Heart":
        heart_card = card_deal_dealer(
            random_card, heart_card, picked_card, random_card_value, random_symbol)


# def card_deal_dealer

def card_deal_dealer(random_card, list_given, picked_card, random_card_value, random_symbol):
    global spade_card
    global heart_card
    global club_card
    global diamond_card
    if random_card in list_given:
        list_given = [x for x in list_given if x != random_card]
        print_picked_card(picked_card)
        card_count_dealer(random_card_value)
        if random_symbol == "Spade":
            spade_card = list_given
            print(spade_card)
        elif random_symbol == "Club":
            club_card = list_given
            print(club_card)
        elif random_symbol == "Diamond":
            diamond_card = list_given
            print(diamond_card)
        elif random_symbol == "Heart":
            heart_card = list_given
            print(heart_card)
    else:
        print_already_dealed()
        pick_card_dealer()


# printing picked card
def print_picked_card(picked_card):
    print("This is the picked Card" + str(picked_card))


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

# counting dealer_card


card_counted_dealer = 0


def card_count_dealer(value):
    global card_counted_dealer
    value = int(value)
    card_counted_dealer += value
    print("This is the card_count_dealer: " + str(card_counted_dealer))
    if card_counted_dealer > 21:
        print("You lost!")
        card_counted_dealer = 0
    print("")


deal_card_btn = tk.Button(app, text="deal card", command=pick_card)
deal_card_btn.grid(row=0, column=1)
start_card_btn = tk.Button(app, text="start game", command=start_game)
start_card_btn.grid(row=1, column=1)
shuffle_btn = tk.Button(app, text="Shuffle", command=shuffle)
shuffle_btn.grid(row=2, column=1)

app.mainloop()
