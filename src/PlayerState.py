import random
from typing import List

from Card import Card

class PlayerState:
    def __init__(self, deck: List[Card], name: str):
        self.name = name

        self.score = 0
        self.deck = deck
        self.discard = []
        self.hand = []
        self.inkwell = []
        self.has_inked = False
        self.field = []
        self.items = []

        self.shuffle()
        for i in range(7):
            self.draw()

    def ready(self):
        self.used_ink = 0
        self.has_inked = False
        for card in self.field:
            card.is_drying = False
            card.is_exhausted = False
        for card in self.inkwell:
            card.is_exhausted = False

    def set(self):
        pass

    def draw(self):
        self.hand.append(self.deck.pop())

    def add_points(self, points):
        self.score += points

    def shuffle(self):
        random.shuffle(self.deck)

    def discard(self, index):
        self.discard.append(self.hand.pop(index))

    def banish(self, index):
        self.discard.append(self.field.pop(index))

    def get_available_ink(self):
        available_ink = 0
        for card in self.inkwell:
            if not card.is_exhausted:
                available_ink += 1
        return available_ink

    def try_ink(self, hand_index):
        if hand_index >= len(self.hand):
            print(f"Hand size is {len(self.hand)} but tried to ink index {hand_index}")
            return False

        target_card = self.hand[hand_index]
        if target_card.inkwell:
            self.inkwell.append(self.hand.pop(hand_index))
            print("Inked " + target_card.full_name)
            return True
        else:
            print("Unable to ink " + target_card.full_name)
            return False

    def try_play(self, hand_index):
        if hand_index >= len(self.hand):
            print(f"Hand size is {len(self.hand)} but tried to play index {hand_index}")
            return False

        target_card = self.hand[hand_index]

        if target_card.cost <= self.get_available_ink():
            for card in self.inkwell:
                if not card.is_exhausted:
                    card.is_exhausted = True
            self.field.append(self.hand.pop(hand_index))
            self.field[-1].is_drying = True
            print("Played " + target_card.full_name)
            return True
        else:
            print("Not enough ink to play " + target_card.full_name)
            return False

    def try_quest(self, field_index):
        if field_index >= len(self.field):
            print(f"Field size is {len(self.field)} but tried to quest index {field_index}")
            return False

        target_card = self.field[field_index]

        if target_card.is_exhausted:
            print("Cannot quest an exhausted card")
            return False
        elif target_card.is_drying:
            print("Cannot quest a drying card")
            return
        elif target_card.lore <= 0:
            print("Cannot quest a card with no lore")
            return False
        else:
            target_card.is_exhausted = True
            self.add_points(target_card.lore)
            print("Quested " + target_card.full_name + " for " + str(target_card.lore) + " lore")
            return True


    def shuffle_in(self, card):
        self.deck.append(card)
        self.shuffle()

    def format_card(self, card: Card):
        return(f"{card.full_name} \n   inkable: {card.inkwell}, cost: {card.cost}, lore: {card.lore}")

    def print_state(self):
        print(f"{self.name} has {self.score} points")
        print(f"{self.name} has {self.get_available_ink()} available of {len(self.inkwell)} total ink")
        print(f"{self.name} has {len(self.deck)} cards in deck")
        print(f"{self.name} has {len(self.hand)} cards in hand")
        print(f"{self.name} has {len(self.field)} cards in field")
        print(f"{self.name} has {len(self.discard)} cards in discard")
        print(f"{self.name} has {len(self.items)} items")

        print("")
        print("In hand:")
        for i, card in enumerate(self.hand):
            print(f"{i}: {self.format_card(card)}")

        print("")
        print("In field:")
        for i, card in enumerate(self.field):
            print(f"{i}: {self.format_card(card)}")
        print("")