import re
from enum import IntEnum

import numpy as np
import pandas as pd


class HandTypes(IntEnum):
    FIVE = 0
    FOUR = 1
    FULL_HOUSE = 2
    THREE = 3
    TWO_PAIR = 4
    ONE_PAIR = 5
    HIGH_CARD = 6


CARD_STRENGTHS = ('A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2')
CARD_STRENGTHS_JOKER = ('A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J')


class Hand:
    def __init__(self, cards: str, bid: int):
        self.cards = cards
        self.bid = bid

    def type(self):
        card_count = self.card_count()
        if card_count == [5]:
            return HandTypes.FIVE
        if card_count == [4, 1]:
            return HandTypes.FOUR
        if card_count == [3, 2]:
            return HandTypes.FULL_HOUSE
        if card_count == [3, 1, 1]:
            return HandTypes.THREE
        if card_count == [2, 2, 1]:
            return HandTypes.TWO_PAIR
        if card_count == [2, 1, 1, 1]:
            return HandTypes.ONE_PAIR
        return HandTypes.HIGH_CARD

    def card_count(self):
        card_count = [self.cards.count(i) for i in set(self.cards)]
        card_count.sort(reverse=True)
        return card_count

    def values(self):
        return [CARD_STRENGTHS.index(card) for card in self.cards]

    def score(self):
        return [int(self.type())] + self.values()

    def to_dict(self):
        dict_ = {}
        for i, s in enumerate(self.score()):
            dict_[f"{i}"] = s
        dict_["bid"] = self.bid
        return dict_


class HandJoker(Hand):
    def card_count(self):
        if self.cards == "JJJJJ":
            return [5]
        number_of_jokers = len(re.findall(r'J', self.cards))
        cards_without_jokers = self.cards.replace('J', '')
        card_count = [cards_without_jokers.count(i) for i in set(cards_without_jokers)]
        card_count.sort(reverse=True)
        card_count[0] += number_of_jokers
        return card_count

    def values(self):
        return [CARD_STRENGTHS_JOKER.index(card) for card in self.cards]


def load_data(filename):
    with open(filename, 'r') as file:
        hands = []
        for line in file:
            cards, bid = line.split(' ')
            hands.append(Hand(cards.strip(), int(bid.strip())))
        return hands


def to_dataframe(hands: list[Hand]):
    return pd.DataFrame([hand.to_dict() for hand in hands])


def rank_hands(hands: list[Hand]):
    df = to_dataframe(hands)
    df = df.sort_values([str(i) for i in range(6)], ascending=[False]*6)
    df = df.reset_index()
    return df


def get_result(hands: list[Hand]):
    bids = np.array(rank_hands(hands).loc[:, 'bid'].values)
    ranks = np.arange(1, len(bids)+1)
    return np.dot(bids, ranks)


def load_data_2(filename):
    with open(filename, 'r') as file:
        hands = []
        for line in file:
            cards, bid = line.split(' ')
            hands.append(HandJoker(cards.strip(), int(bid.strip())))
        return hands


def main():
    data = load_data("data.txt")
    print(get_result(data))
    data_2 = load_data_2("data.txt")
    print(get_result(data_2))


if __name__ == '__main__':
    main()
