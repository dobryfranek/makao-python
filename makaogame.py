class Makao():
    def __init__(self, num_players: int, num_decks: int = 1):
        self.card_amount = 52 * num_decks
        self.colors = ["kier", "pik", "karo", "trefl"]
        self.values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "Q", ]