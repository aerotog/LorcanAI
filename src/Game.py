import random
from typing import List, Tuple
from Actions import Actions
from AllCards import AllCards
from Card import Card
from PlayerState import PlayerState




class Game:
    def __init__(self,
                 deck_tuples1: List[Tuple[str, str]],
                 deck_tuples2: List[Tuple[str, str]]):

        self.cards = AllCards()

        deck1 = self.convert_deck_to_cards(deck_tuples1)
        self.player1 = PlayerState(deck1, "Player 1")

        deck2 = self.convert_deck_to_cards(deck_tuples2)
        self.player2 = PlayerState(deck2, "Player 2")

        self.active_player = self.player1

        self.prior_action = None
        self.awaiting_target = False
        self.has_inked = False
        self.turn_count = 1

    def convert_deck_to_cards(self, deck_tuples: List[Tuple[str, str]]) -> List[Card]:
        cards = []
        for dt in deck_tuples:
            card = self.cards.get_from_name(dt[0])
            for i in range(dt[1]):
                cards.append(card)

        return cards

    def check_winner(self):
        score_limit = 20

        if self.player1.score >= score_limit:
            return self.player1
        elif self.player2.score >= score_limit:
            return self.player2
        else:
            return None

    def pass_turn(self):
        self.active_player = self.get_other_player()
        # print(f"Turn passed to {self.active_player.name}")
        self.has_inked = False
        self.turn_count += 1

        self.active_player.ready()
        self.active_player.set()
        self.active_player.draw()


    def get_other_player(self):
        if self.active_player == self.player1:
            return self.player2
        else:
            return self.player1

    def do_random_command(self):
        if self.awaiting_target:
            if self.prior_action == Actions.INK:
                if len(self.active_player.hand) > 0:
                    for i,card in enumerate(self.active_player.hand):
                        if card.inkwell == True:
                            self.do_command(i)

            if self.prior_action == Actions.PLAY:
                if len(self.active_player.hand) > 0:
                    self.do_command(random.randint(0, len(self.active_player.hand) - 1))

            if self.prior_action == Actions.QUEST:
                if len(self.active_player.field) > 0:
                    self.do_command(random.randint(0, len(self.active_player.field) - 1))

            self.awaiting_target = False
        else:
            action_count = len(Actions)-1
            random_action = random.randint(-1, action_count)
            self.do_command(random_action)

    def do_command(self, target: int):
        if self.awaiting_target:
            card = target

            if target == Actions.PASS.value:
                print(">>> CANCELING ACTION <<<" )
                self.awaiting_target = False

            if self.prior_action == Actions.INK:
                if self.active_player.try_ink(card):
                    self.active_player.has_inked = True
                    self.awaiting_target = False

            if self.prior_action == Actions.PLAY:
                if self.active_player.try_play(card):
                    self.awaiting_target = False

            if self.prior_action == Actions.QUEST:
                if self.active_player.try_quest(card):
                    self.awaiting_target = False
            return

        action = target

        if action == Actions.PASS.value:
            if not self.awaiting_target:
                self.pass_turn()

        elif action == Actions.INK.value:
            if self.active_player.has_inked:
                print(">>> ALREADY INKED THIS TURN <<<")
            else:
                self.prior_action = Actions.INK
                self.awaiting_target = True
                print(">>> SELECT CARD TO INK <<<")
                # self.active_player.print_state()

        elif action == Actions.PLAY.value:
            self.prior_action = Actions.PLAY
            self.awaiting_target = True
            print(">>> SELECT CARD TO PLAY <<<")
            # self.active_player.print_state()

        elif action == Actions.QUEST.value:
            self.prior_action = Actions.QUEST
            self.awaiting_target = True
            print(">>> SELECT CARD TO QUEST <<<")
            # self.active_player.print_state()

    def print_state(self):
        print("Active player: " + self.active_player.name)
        print("Turn: " + str(self.turn_count))


