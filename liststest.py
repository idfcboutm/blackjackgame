from cgi import test
from cards import spade_card


def test_list(list_test, random_card):
    list_test = [x for x in list_test if x != random_card]
    return list_test


print(spade_card)

spade_card = test_list(spade_card, "3")

print(spade_card)
