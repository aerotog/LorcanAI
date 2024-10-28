import json
from typing import List

from Card import Card

class AllCards:
    def __init__(self):
        # self.cards = List[Card]
        self.cards = {}
        self.load_cards()

    def load_cards(self):
        with open('./cards/allCards.json') as f:
            cards_from_json = json.load(f)["cards"]

            # print(cards_from_json[0])

            for c in cards_from_json:
                card = Card.from_dict(c)
                # self.cards.append(card)
                self.cards[card.id] = card

    def get_from_name(self, full_name) -> int:
        for id,card in self.cards.items():
            if card.full_name.lower() == full_name.lower():
                return card

        print("UNABLE TO FIND CARD WITH NAME " + full_name)

    def get_by_id(self, id: int) -> Card:
        return self.id_to_card[id]