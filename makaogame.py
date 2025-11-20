class Makao():
    def __init__(self, num_players: int = 4, num_decks: int = 1, use_english: bool = False):
        self.card_amount = 52 * num_decks
        self.colors = ["heart", "spade", "diamond", "club"] if use_english else ["kier", "pik", "karo", "trefl"]
        self.values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "Q", "J", "K"]
        self.num_players = num_players
