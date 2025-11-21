from random import shuffle

MAKAO_COLORS = ["kier", "pik", "karo", "trefl"]
MAKAO_VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "Q", "J", "K"]

class Card():
    def __init__(self, color: str, value: str):
        assert color in MAKAO_COLORS and value in MAKAO_VALUES
        self.color = color
        self.value = value

class Player():
    def __init__(self, name: str = "undefined", hand: list[tuple] = []):
        self.name = name
        self.hand = hand


class Makao():
    def __init__(self, players: list[Player] = [Player() for _ in range(4)], num_decks: int = 1):
        self.card_amount = 52 * num_decks

        self.colors = MAKAO_COLORS
        self.values = MAKAO_VALUES

        self.num_players = len(players)
        self.player_hands = {player: [] for player in players} # wywal
        self.current_turn = 0
        self.reserve_deck = []
        self.played_deck = []
        self.create_deck()
    
    def create_deck(self):
        for deck in range(self.card_amount // 52):
            for value in self.values:
                for color in self.colors:
                    self.reserve_deck.append(Card(color, value))
        shuffle(self.reserve_deck)
        shuffle(self.reserve_deck)
        shuffle(self.reserve_deck)
        for c in self.reserve_deck:
            print(c.color, c.value)

if __name__ == "__main__": # for test
    macau = Makao()